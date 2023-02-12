from simple_model import User, SessionLocal
if __name__ == '__main__':
    # user = User(name="Antonio", surname="Banderos", age=36)
    session = SessionLocal()
    # session.add(user)
    for user in (
            session.query(User)\
                    .filter(User.age > 19)\
                    .all()
    ):
        print(user.id, user.name, user.age)