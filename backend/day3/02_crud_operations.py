# DAY 3 — EXERCISE 2: CRUD Operations
#
# TASK: Practice the four database operations (Create, Read, Update, Delete)
# using SQLAlchemy sessions. A session is a unit-of-work — changes are staged
# locally and only written to the DB when you call session.commit().
#
# STEPS:
#   1. Implement create_user() — add a User to the session and commit
#   2. Implement get_user_by_username() — query by username, return User or None
#   3. Implement update_email() — find user, change email, commit
#   4. Implement delete_user() — find user, delete, commit
#   5. Run:
#        $ uv run python day3/02_crud_operations.py
#
# EXPECTED OUTPUT:
#   Created: User(id=1, username='alice', email='alice@example.com')
#   Found:   User(id=1, username='alice', email='alice@example.com')
#   Updated: alice → new email: alice@chat.app
#   Deleted: alice
#   After delete: None

from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

DATABASE_URL = "sqlite:///chat_crud.db"
engine = create_engine(DATABASE_URL)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    def __repr__(self):
        return f"User(id={self.id}, username={self.username!r}, email={self.email!r})"


Base.metadata.create_all(engine)


def create_user(
    session: Session, username: str, email: str, password_hash: str
) -> User:
    # TODO: create User, add to session, commit, refresh, return
    user = User(username=username, email=email, password_hash=password_hash)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def get_user_by_username(session: Session, username: str) -> User | None:
    # TODO: use session.execute(select(User).where(...)) and return scalar result
    # result = session.execute(
    #     select(User).where(User.username == username)
    # )

    # return result.scalar_one_or_none()

    return session.execute(select(User).where(User.username == username)).scalar()


def update_email(session: Session, username: str, new_email: str) -> User | None:
    user = get_user_by_username(session, username)
    if user is None:
        return None
    user.email = new_email
    session.commit()
    session.refresh(user)

    return user


def delete_user(session: Session, username: str) -> bool:
    user = get_user_by_username(session, username)
    if user is None:
        return False
    session.delete(user)
    session.commit()
    return True


if __name__ == "__main__":
    with Session(engine) as session:
        user = create_user(session, "alice", "alice@example.com", "hashed_pw")
        print(f"Created: {user}")

        found = get_user_by_username(session, "alice")
        print(f"Found:   {found}")

        updated = update_email(session, "alice", "alice@chat.app")
        print(f"Updated: alice → new email: {updated.email}")

        delete_user(session, "alice")
        print("Deleted: alice")

        after = get_user_by_username(session, "alice")
        print(f"After delete: {after}")
