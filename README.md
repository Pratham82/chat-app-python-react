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

| Phase | Topic |
|---|---|
| 1 | Python async, FastAPI, PostgreSQL, JWT auth, React shell |
| 2 | WebSocket fundamentals, connection lifecycle, event protocol |
| 3 | Chat MVP — messaging, history, optimistic UI |
| 4 | Realtime UX — typing indicators, presence, read receipts, reconnect |
| 5 | Architecture cleanup — backend structure, Zustand store, error handling |
| 6 | Group chat — rooms, memberships, group broadcasting |
| 7 | Production reliability — heartbeats, deduplication, rate limiting |
| 8 | Scaling — Redis pub/sub, multi-instance messaging |
| 9 | Deployment — Docker Compose, cloud hosting |

See `project.md` for the full day-by-day curriculum.

## Running the backend

```bash
cd backend
uv run python day1/01_sequential_vs_concurrent.py
```

Requires Python 3.14+ and [uv](https://docs.astral.sh/uv/).

## Stack

- **Backend:** Python 3.14, FastAPI, SQLAlchemy (async), asyncpg, Alembic, bcrypt, python-jose
- **Frontend:** React, TypeScript, Vite, Tailwind, Zustand, React Router *(not yet scaffolded)*
- **Infrastructure:** PostgreSQL, Redis, Docker Compose
