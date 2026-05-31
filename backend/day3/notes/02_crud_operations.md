# Notes: 02_crud_operations.py

**Date:** 2026-05-31

## Key concepts

- A SQLAlchemy `Session` is a unit-of-work: changes (`add`, `delete`, mutations) are staged in memory and only written to the DB on `session.commit()` — like a git staging area where `commit()` is the actual write
- `session.refresh(user)` reloads the object from the DB after a commit, pulling back any DB-generated values (e.g. auto-incremented `id`) — without it the ORM object may have stale or missing fields
- `select(User).where(User.username == username)` is SQLAlchemy's typed query builder — equivalent to `SELECT * FROM users WHERE username = ?`; the result is a `Result` object you call `.scalar()` or `.scalar_one_or_none()` on to get the ORM instance
- `Base.metadata.create_all(engine)` at module level is a quick dev shortcut — it creates all tables if they don't exist; in production this is replaced by Alembic migrations

## Gotchas / nuances

- `.scalar()` and `.scalar_one_or_none()` both return `None` if no row is found, but `.scalar_one_or_none()` raises if there are *multiple* rows — safer for unique-column queries like username lookups
- Mutating an ORM object that's already in the session (e.g. `user.email = new_email`) is enough — no `session.add()` needed for updates, SQLAlchemy tracks "dirty" objects automatically
- `with Session(engine) as session` does NOT auto-commit on exit — it only closes/returns the connection; you still need explicit `session.commit()` calls inside
- Running the script twice without deleting `chat_crud.db` will raise a `UNIQUE constraint failed` error on `username` — the DB persists between runs
