import pandas as pd
from loguru import logger
from sqlalchemy import create_engine
liked_posts = pd.read_csv('liked_posts', sep=';')

print(f"liked_posts загружено в RAM: {liked_posts.shape}")


# liked_posts.to_sql(
#    "antonio_st_liked_posts_lesson_22",
#     con="postgresql://robot-startml-ro:pheiph0hahj1Vaif@"
#         "postgres.lab.karpov.courses:6432/startml",
#     schema="public",
#     if_exists='replace'
#    )
# print('Загрузка завершена')


engine = create_engine(
    "postgresql://robot-startml-ro:pheiph0hahj1Vaif@"
    "postgres.lab.karpov.courses:6432/startml"
)

conn = engine.connect().execution_options(stream_results=True)
CHUNKSIZE = 200000
liked_posts.to_sql(name='antonio_st_liked_posts_lesson_22',
                   schema="public",
                   con=engine,
                   if_exists='replace',
                   chunksize=CHUNKSIZE)

print('Загрузка завершена')
