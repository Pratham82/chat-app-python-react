# Python + React WebSocket Chat App

A structured self-learning curriculum to build a production-style WhatsApp-like chat app. See `project.md` for the full 44-day plan across 9 phases.

**Current phase:** Day 1 — async Python fundamentals (`backend/day1/`).

## Running exercises

All backend commands use `uv` from the `backend/` directory:

```bash
uv run python day1/01_sequential_vs_concurrent.py
uv run python day1/02_fake_api_fetch.py
```

To run the main entry point:

```bash
uv run python main.py
```

## Exercise conventions

- Each exercise file has a `TASK` comment block with instructions and expected output.
- Notes live in `notes/<exercise-filename>.md` next to the exercise file (e.g. `day1/notes/01_sequential_vs_concurrent.md`).
- Notes template: **Key concepts** (the "why") + **Gotchas / nuances** (subtle behavior).

## Skills

Skills are in `.claude/skills/` — opencode reads them natively:

- **`exercise-review`** — runs the exercise with `uv run python`, compares output to expected, reports pass/fail.
- **`take-notes`** — extracts key concepts and gotchas into a `notes/` markdown file.

## Tech stack

| Layer           | Stack                                                    |
| --------------- | -------------------------------------------------------- |
| Backend runtime | Python 3.14+, FastAPI, Uvicorn                           |
| ORM / DB        | SQLAlchemy (async), asyncpg, PostgreSQL                  |
| Auth            | bcrypt, python-jose (JWT)                                |
| Migrations      | Alembic                                                  |
| Realtime        | WebSockets (FastAPI native), Redis pub/sub (Phase 8)     |
| Frontend        | React, TypeScript, Vite, Tailwind, Zustand, React Router |
| Package manager | `uv` (backend), `npm`/`pnpm` (frontend, not yet built)   |
| Deployment      | Docker Compose, Railway/Render/Fly.io + Vercel           |

## Planned backend structure (from Day 21)

```
backend/
  app/
    websocket/
      manager.py    # connection tracking
      handlers.py   # message routing
      events.py     # event type definitions
```

## WebSocket event protocol

Messages use a typed envelope (not bare strings):

```json
{ "type": "message" | "typing" | "presence" | "read_receipt" | "join_room" | "leave_room", "payload": {} }
```
