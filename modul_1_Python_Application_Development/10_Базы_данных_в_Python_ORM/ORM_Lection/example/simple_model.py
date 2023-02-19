from sqlalchemy import Column, Integer, String, create_engine, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:26252@localhost:5432/postgres"

#  прослойка, для БД
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# создание сессии для подключения к БД
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#metadata_obj = MetaData()
Base = declarative_base()

class User(Base):
    __tablename__ = "users.copy"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    age = Column(Integer)

# в коде использована версия ORM 2.0.2 с обновленным синтакисом
# https://docs.sqlalchemy.org/en/14/core/metadata.html

# User = Table(
#     "users.copy",
#     metadata_obj,
#     Column("id", Integer, primary_key=True),
#     Column("name", String),
#     Column("surname", String),
#     Column("age", Integer)
# )

# выполнить только при запуске скрипта, но не при импорте
if __name__ == '__main__':
    user = User(name="Cristopher", surname="Lloyd", age=84)
    session = SessionLocal()
    session.add(user)
    session.commit()
    # обратиться к Base, вызвать разметку таблицы и вызов прослойки для БД
    # Base.metadata.create_all(engine)
    #User.create(engine)