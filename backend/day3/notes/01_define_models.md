# Notes: 01_define_models.py

**Date:** 2026-05-31

## Key concepts

- SQLAlchemy's declarative ORM maps Python classes → DB tables: the class is the table, class attributes are columns — analogous to a TypeScript class with decorators in TypeORM
- `DeclarativeBase` is the modern (2.0+) base class — all models inherit from it so SQLAlchemy knows to track them in `Base.metadata`
- `Mapped[type]` + `mapped_column(...)` is the typed column syntax: `Mapped[int]` tells both Python and SQLAlchemy the column type, replacing the older `Column(Integer, ...)` style
- `Base.metadata.create_all(engine)` inspects all registered models and issues `CREATE TABLE IF NOT EXISTS` DDL — quick for dev/learning, replaced by Alembic in production

## Gotchas / nuances

- `server_default=func.now()` runs `now()` on the DB side at insert time — use this (not `default=datetime.now`) so the timestamp is set by the DB, not the Python process clock
- `Mapped[str]` on `created_at` is a type annotation mismatch — the column is `DateTime` but annotated as `str`; should be `Mapped[datetime]`. It works at runtime but will cause type-checker warnings
- `Base.metadata.create_all` is idempotent — running the script twice won't duplicate the table, but schema changes (added columns) won't be applied either; that's what Alembic is for
- `inspect(engine).get_columns("users")` is a handy introspection tool for verifying the actual DB schema matches your model — useful for debugging migration issues
