from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from table_user import User
from table_post import Post

class Feed(Base):
    __tablename__ = "feed_action"
    user_id = Column(
        Integer, ForeignKey("user.id"), primary_key=True, name="user_id"
    )
    post_id = Column(
        Integer, ForeignKey("post.id"), primary_key=True, name="post_id"
    )
    action = Column(String)
    time = Column(TIMESTAMP, name="time")
    user = relationship(User)
    post = relationship(Post)