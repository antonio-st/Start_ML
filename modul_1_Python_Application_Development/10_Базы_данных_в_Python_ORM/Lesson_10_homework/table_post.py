from database import Base, SessionLocal
from sqlalchemy import Column, Integer, String,Text


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    text = Column(Text)
    # nullable разрешает пропускать значение в колонке
    topic = Column(String, nullable=True)

    # печатать объект
    def __repr__(self):
        return f"{self.id} - {self.topic}"

if __name__ == "__main__":
    session = SessionLocal()
    list_post = []
    for post in (
            session.query(Post)
                    .filter(Post.topic == "business")
                    .order_by(Post.id.desc())
                    .limit(10)
                    .all()
    ):
        list_post.append(post.id)
    print(list_post)






