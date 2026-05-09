# DAY 3 — EXERCISE 1: Define SQLAlchemy Models
#
# TASK: Define the User model for the chat app using SQLAlchemy's
# declarative ORM. SQLAlchemy maps Python classes → database tables.
#
# STEPS:
#   1. Complete the User model — add the missing columns:
#      - email:         String, unique, not null
#      - password_hash: String, not null
#      - created_at:    DateTime, defaults to now (use func.now())
#   2. Run the script — it creates a local SQLite file and prints the schema:
#        $ uv run python day3/01_define_models.py
#   3. Open chat.db with any SQLite viewer (or sqlite3 CLI) to confirm the table:
#        $ sqlite3 chat.db ".schema"
#
# EXPECTED OUTPUT:
#   Table 'users' created.
#   Columns: id, username, email, password_hash, created_at
#   Sample user (not persisted): User(id=None, username='alice', email='alice@example.com')

from sqlalchemy import DateTime, String, create_engine, func, inspect
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

DATABASE_URL = "sqlite:///chat.db"
engine = create_engine(DATABASE_URL)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    # TODO: add email (String, unique, not null)
    # TODO: add password_hash (String, not null)
    # TODO: add created_at (DateTime, server_default=func.now())

    def __repr__(self):
        return f"User(id={self.id}, username={self.username!r}, email={self.email!r})"


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    inspector = inspect(engine)
    cols = [c["name"] for c in inspector.get_columns("users")]
    print("Table 'users' created.")
    print(f"Columns: {', '.join(cols)}")

    sample = User(username="alice", email="alice@example.com", password_hash="<hashed>")
    print(f"Sample user (not persisted): {sample}")
