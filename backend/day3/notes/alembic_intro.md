# Notes: alembic_intro.py

**Date:** 2026-05-31

## Key concepts

- Alembic is "git for your database schema" — it tracks schema changes as versioned migration files so you can apply, roll back, and share DB changes across environments
- `alembic init alembic` scaffolds the `alembic/` folder and `alembic.ini`; you only run this once per project
- `env.py` is the wiring layer: you point `target_metadata` at your `Base.metadata` so Alembic can diff your models against the live DB and auto-generate migrations
- `alembic revision --autogenerate` compares models → DB and writes the `upgrade()` / `downgrade()` SQL for you; `alembic upgrade head` actually applies it
- SQLite stores the entire DB (tables, data, indexes) in a single `.db` file — no server needed, great for local dev. Swap the URL to `postgresql+asyncpg://...` for production; everything else stays the same

## Gotchas / nuances

- `config.set_main_option("sqlalchemy.url", "sqlite:///chat_alembic.db")` must be in `env.py` — if you skip it, the placeholder URL from `alembic.ini` (`driver://user:pass@localhost/dbname`) reaches the engine and causes a cryptic load error at `run_env()`
- The URL override must come **after** `config = context.config`, not before — `config` doesn't exist yet on the lines above it
- Python can't import filenames starting with a digit (e.g. `04_alembic_intro.py`) — rename to `alembic_intro.py` before using it in an `env.py` import
- `sqlite:///` (3 slashes) = relative path; `sqlite:////` (4 slashes) = absolute path
- The `from day3.alembic_intro import Base` import in `env.py` only works when `uv run alembic` is invoked from the `backend/` directory, because that's what gets added to `sys.path`
