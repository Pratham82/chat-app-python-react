# Chat App — Python + React

A structured learning project to build a production-style WhatsApp-like chat app from scratch.

## What's being built

A real-time chat application with:

- FastAPI WebSocket backend
- React + TypeScript frontend
- PostgreSQL for persistence
- Redis pub/sub for horizontal scaling
- JWT authentication

## Learning phases

| Phase | Topic                                                                   |
| ----- | ----------------------------------------------------------------------- |
| 1     | Python async, FastAPI, PostgreSQL, JWT auth, React shell                |
| 2     | WebSocket fundamentals, connection lifecycle, event protocol            |
| 3     | Chat MVP — messaging, history, optimistic UI                            |
| 4     | Realtime UX — typing indicators, presence, read receipts, reconnect     |
| 5     | Architecture cleanup — backend structure, Zustand store, error handling |
| 6     | Group chat — rooms, memberships, group broadcasting                     |
| 7     | Production reliability — heartbeats, deduplication, rate limiting       |
| 8     | Scaling — Redis pub/sub, multi-instance messaging                       |
| 9     | Deployment — Docker Compose, cloud hosting                              |

See `project.md` for the full day-by-day curriculum.

## Progress checklist — Day 1 to Day 4

### Day 1 — Async Python

- [ ] `async` / `await` syntax and coroutines
- [ ] Event loop — what it is and how it works
- [ ] Blocking vs non-blocking code
- [ ] Concurrency with `asyncio.create_task()`
- [ ] Running multiple tasks with `asyncio.gather()`
- [ ] Task cancellation
- [ ] Timeouts
- [ ] Exception handling in async code

**Exercises**

- [x] `day1/01_sequential_vs_concurrent.py`
- [x] `day1/02_fake_api_fetch.py`
- [x] `day1/03_tasks_and_cancellation.py`
- [x] `day1/04_timeouts.py`

---

### Day 2 — FastAPI Basics

- [ ] Routes and request/response lifecycle
- [ ] Path params and query params
- [ ] Request body with Pydantic models
- [ ] Response models
- [ ] Dependency injection
- [ ] Input validation

**Exercises**

- [x] `day2/01_first_route.py`
- [x] `day2/02_path_and_query_params.py`
- [x] `day2/03_request_body_and_models.py`
- [x] `day2/04_dependency_injection.py`

**Build**

- [ ] `GET /health`
- [ ] `GET /users`
- [ ] `POST /users`
- [ ] `GET /users/:id`

---

### Day 3 — Database + ORM

- [ ] PostgreSQL basics
- [ ] SQLAlchemy ORM (sync and async)
- [ ] Sessions and transactions
- [ ] Alembic migrations

**Exercises**

- [x] `day3/01_define_models.py`
- [x] `day3/02_crud_operations.py`
- [x] `day3/03_async_session.py`
- [x] `day3/04_alembic_intro.py`

**Build**

- [ ] `users` table with `id`, `username`, `email`, `password_hash`, `created_at`

---

### Day 4 — Authentication

- [ ] Password hashing with bcrypt
- [ ] JWT structure and signing
- [ ] Access tokens and expiry
- [ ] Protected routes
- [ ] Dependency-based auth in FastAPI

**Exercises**

- [ ] `day4/01_password_hashing.py`
- [ ] `day4/02_jwt_tokens.py`
- [ ] `day4/03_auth_routes.py`
- [ ] `day4/04_protected_routes.py`

**Build**

- [ ] `POST /signup`
- [ ] `POST /login`
- [ ] `GET /me`

## Running the backend

```bash
cd backend
uv run python day1/01_sequential_vs_concurrent.py
```

Requires Python 3.14+ and [uv](https://docs.astral.sh/uv/).

## Stack

- **Backend:** Python 3.14, FastAPI, SQLAlchemy (async), asyncpg, Alembic, bcrypt, python-jose
- **Frontend:** React, TypeScript, Vite, Tailwind, Zustand, React Router _(not yet scaffolded)_
- **Infrastructure:** PostgreSQL, Redis, Docker Compose
