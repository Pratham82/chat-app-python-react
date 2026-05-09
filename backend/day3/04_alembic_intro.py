# DAY 3 — EXERCISE 4: Alembic Migrations
#
# TASK: Alembic manages schema changes over time (like git for your DB).
# This exercise walks through the real alembic workflow you'll use in the app.
#
# STEPS — run each command from the backend/ directory:
#
#   1. Initialise Alembic (creates alembic/ folder + alembic.ini):
#        $ uv run alembic init alembic
#
#   2. Edit alembic/env.py — replace the two placeholder lines:
#        # find this line:
#        target_metadata = None
#        # replace with:
#        from day3.04_alembic_intro import Base
#        target_metadata = Base.metadata
#
#      Also set the DB URL — find:
#        config.set_main_option("sqlalchemy.url", ...)
#      and point it at SQLite:
#        config.set_main_option("sqlalchemy.url", "sqlite:///chat_alembic.db")
#
#   3. Generate your first migration (auto-detects the models below):
#        $ uv run alembic revision --autogenerate -m "create users table"
#
#   4. Apply it:
#        $ uv run alembic upgrade head
#
#   5. Confirm:
#        $ sqlite3 chat_alembic.db ".schema"
#        → should show CREATE TABLE users (...)
#
#   6. Add a new column to User below (e.g. is_active: Mapped[bool] = ...),
#      then generate and apply a second migration:
#        $ uv run alembic revision --autogenerate -m "add is_active to users"
#        $ uv run alembic upgrade head
#
#   7. View migration history:
#        $ uv run alembic history
#
# EXPECTED HISTORY OUTPUT (step 7):
#   <rev2> -> head (head), add is_active to users
#   <rev1> -> <rev2>, create users table

from sqlalchemy import Boolean, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    # TODO (step 6): add is_active: Mapped[bool] = mapped_column(Boolean, default=True)
