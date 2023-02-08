from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from table_post import Post
from table_user import User
from table_feed import Feed
from schema import UserGet, PostGet, FeedGet
from typing import List
from loguru import logger
from sqlalchemy import func

app = FastAPI()


def get_db():
    with SessionLocal() as db:
        return db


@app.get("/user/{id}", response_model=UserGet)
def get_user(id: int, db: Session = Depends(get_db)):
    results = db.query(User) \
        .filter(User.id == id) \
        .first()
    if results:
        return results
    else:
        raise HTTPException(404, "user not found")


@app.get("/post/{id}", response_model=PostGet)
def get_post(id: int, db: Session = Depends(get_db)):
    results = db.query(Post) \
        .filter(Post.id == id) \
        .first()
    if results:
        return results
    else:
        raise HTTPException(404, "user not found")


@app.get("/user/{id}/feed", response_model=List[FeedGet])
def get_feed_user(id: int, limit: int = 10, db: Session = Depends(get_db)):
    results = db.query(Feed).filter(Feed.user_id == id).order_by(Feed.time.desc()).limit(limit).all()
    # logger.info(type(results))
    #logger.info(len(results))
    return results


@app.get("/post/{id}/feed", response_model=List[FeedGet])
def get_feed_post(id: int, limit: int = 10, db: Session = Depends(get_db)):
    results = db.query(Feed).filter(Feed.post_id == id).order_by(Feed.time.desc()).limit(limit).all()
    # logger.info(type(results))
    logger.info(len(results))
    return results


@app.get("/post/recommendations/", response_model=List[PostGet])
def get_feed_like(id: int = 100, limit: int = 10, db: Session = Depends(get_db)):
    result = db.query(Post).select_from(Feed).filter(Feed.action == 'like').join(Post) \
        .group_by(Post.id).order_by(func.count(Post.id).desc()).limit(limit).all()
    return result
