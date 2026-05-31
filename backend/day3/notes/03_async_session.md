# Notes: 03_async_session.py

**Date:** 2026-05-31

## Key concepts

- `async_sessionmaker` + `AsyncSession` is the async equivalent of SQLAlchemy's regular `Session` — same API, but every DB call is `await`ed
- `Depends(get_session)` is FastAPI's dependency injection: the session is created per-request, yielded to the route, and cleaned up after — like middleware but scoped to a single handler
- `get_session()` is an async generator (uses `yield`) so FastAPI can run teardown (the `finally` block) after the response is sent — analogous to a `try/finally` around an Express middleware's `next()`
- `expire_on_commit=False` on `async_sessionmaker` prevents SQLAlchemy from expiring (invalidating) ORM objects after `commit()`, which would trigger lazy-load errors in async context since there's no implicit I/O allowed

## Gotchas / nuances

- `async with SessionLocal() as session` already calls `session.close()` on exit — the explicit `await session.close()` in `finally` is redundant but harmless; the `async with` form is the cleaner pattern
- `session.get(User, user_id)` fetches by primary key directly (no `select` needed) and returns `None` if not found — use this over `select` + `.scalar_one_or_none()` for PK lookups
- `await session.refresh(new_user)` is needed after `commit()` to reload DB-generated fields (e.g. `id`, `created_at`) back onto the ORM object before returning it
- `select(User.id, User.username, User.email)` returns column tuples, not ORM objects — `.mappings().all()` converts them to dict-like rows safe to serialize; selecting the full `User` model and using `response_model` is the cleaner production pattern
- `@app.on_event("startup")` is deprecated in newer FastAPI — prefer `lifespan` context manager, but the pattern works for learning exercises
- Swap `sqlite+aiosqlite:///` → `postgresql+asyncpg://` and nothing else changes — the async engine abstraction is DB-agnostic
