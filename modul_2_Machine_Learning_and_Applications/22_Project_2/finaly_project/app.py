from fastapi import FastAPI
import pandas as pd
import os
from typing import List
from sqlalchemy import create_engine
from datetime import datetime
from loguru import logger
from sqlalchemy import create_engine
from schema import PostGet
from catboost import CatBoostClassifier


app = FastAPI()


def batch_load_sql(query: str) -> pd.DataFrame:
    CHUNKSIZE = 200000
    engine = create_engine(
        "postgresql://robot-startml-ro:pheiph0hahj1Vaif@"
        "postgres.lab.karpov.courses:6432/startml"
    )
    conn = engine.connect().execution_options(stream_results=True)
    chunks = []
    for chunk_dataframe in pd.read_sql(query, conn, chunksize=CHUNKSIZE):
        chunks.append(chunk_dataframe)
        logger.info(f"Got chunk: {len(chunk_dataframe)}")
    conn.close()
    return pd.concat(chunks, ignore_index=True)


# загружаем модель CatBoost из файла

def get_model_path(path: str) -> str:
    # Проверяем, где выполняется код в лмс, или локально. Немного магии
    if os.environ.get("IS_LMS") == "1":
        MODEL_PATH = '/workdir/user_input/model'
    else:
        MODEL_PATH = path
    return MODEL_PATH


# загружаем данные из таблиц

def load_features():
    # уникальные записи post_id, user_id
    # где он поставил лайк
    logger.info("loading liked user posts")
    liked_posts_query = """
                    SELECT post_id, user_id
                    FROM public.antonio_st_liked_posts_lesson_22"""
    liked_posts = batch_load_sql(liked_posts_query)

    # Загрузим фичи из таблицы antonio_st_features_lesson_22_
    logger.info("loading posts features")
    posts_features = pd.read_sql(
        """SELECT * FROM public.antonio_st_features_lesson_22_""",
        con="postgresql://robot-startml-ro:pheiph0hahj1Vaif@"
            "postgres.lab.karpov.courses:6432/startml"
    )

    # Загрузим фичи по юзерам
    logger.info("loading user features")
    user_features = pd.read_sql(
        """SELECT * 
           FROM public.user_data """,
        con="postgresql://robot-startml-ro:pheiph0hahj1Vaif@"
            "postgres.lab.karpov.courses:6432/startml"
    )
    logger.info(
        f"{liked_posts.shape, posts_features.shape, user_features.shape}")
    return [liked_posts, posts_features, user_features]


def load_models():
    # Загрузка Catboost

    model_path = get_model_path(
        "/home/antonio/#LEARN/Start_ML/modul_2_Machine_Learning_and_Applications/22_Project_2/Next3/catboost_model")
    loaded_model = CatBoostClassifier()
    loaded_model.load_model(model_path)
    return loaded_model


# Положим при поднятии сервиса модель и фичи в переменные
# model и features

logger.info("loading model")
model = load_models()
logger.info("loading features")
features = load_features()
logger.info("service load data and model")


def get_recommended_feed(id: int, time: datetime, limit: int):
    # Загрузка фичей по пользователям
    logger.info(f"user_id: {id}")
    logger.info("reading features")
    user_features = features[2].loc[features[2].user_id == id]
    user_features = user_features.drop('user_id', axis=1)

    # Загружаем фичи по постам
    logger.info("dropping columns")
    posts_features = features[1].drop(['index', 'text'], axis=1)
    content = features[1][['post_id', 'text', 'topic']]

    # Объединим фичи
    logger.info("zipping everything")
    add_user_features = dict(
        zip(user_features.columns, user_features.values[0]))
    logger.info("assigning everything")
    user_posts_features = posts_features.assign(**add_user_features)
    user_posts_features = user_posts_features.set_index('post_id')

    # Добавляем информацию о дате рекомендаций
    logger.info("add time info")
    user_posts_features['hour'] = time.hour
    user_posts_features['month'] = time.month
    logger.info(f"finally_columns: {user_posts_features.shape}")
    logger.info(f"finally_columns: {user_posts_features.columns}")

    # Формируем предсказания вероятности лайкнуть пост
    logger.info('Predicting')
    predicts = model.predict_proba(user_posts_features)[:, 1]
    user_posts_features['predicts'] = predicts

    # Убираем записи где пользователь уже ставил лайк
    logger.info('deleting liked posts')
    liked_posts = features[0]
    liked_posts = liked_posts[liked_posts.user_id == id].post_id.values
    filtered_ = user_posts_features[~user_posts_features.index.isin(
        liked_posts)]

    # Рекомендуем top-5 по вероятности постов
    recommended_posts = filtered_.sort_values('predicts')[-limit:].index

    return [
        PostGet(**{
            "id": i,
            "text": content[content.post_id == i].text.values[0],
            "topic": content[content.post_id == i].topic.values[0]
        }) for i in recommended_posts
    ]


@app.get("/post/recommendations/", response_model=List[PostGet])
def recommended_posts(
        id: int,
        time: datetime,
        limit: int = 10) -> List[PostGet]:
    return get_recommended_feed(id, time, limit)
