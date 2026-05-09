# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project is

A structured self-learning curriculum to build a production-style WebSocket chat app (WhatsApp-like). The program runs ~9 weeks across 9 phases, progressing from Python async basics through FastAPI, WebSockets, PostgreSQL, Redis pub/sub, and deployment. See `project.md` for the full day-by-day plan.

**Current phase:** Day 1 — async Python fundamentals (`backend/day1/`).

## Running exercises

All backend commands use `uv` and must be run from the `backend/` directory:

```bash
cd backend
uv run python day1/01_sequential_vs_concurrent.py
uv run python day1/02_fake_api_fetch.py
```

To run the main entry point:

```bash
cd backend
uv run python main.py
```

## Exercise conventions

- Each exercise file has a `TASK` comment block at the top with instructions and expected output.
- Notes for each exercise live in `notes/<exercise-filename>.md` next to the exercise file (e.g. `day1/notes/01_sequential_vs_concurrent.md`).
- Notes follow the template: **Key concepts** (the "why") + **Gotchas / nuances** (subtle behavior).

## Custom skills

Two skills are available via `/skill`:

- **`/exercise-review`** — runs the exercise with `uv run python`, compares output to the expected output in comments, and reports pass/fail.
- **`/take-notes`** — extracts key concepts and gotchas from an exercise into a `notes/` markdown file.

## Tech stack (planned across the curriculum)

| Layer           | Stack                                                       |
| --------------- | ----------------------------------------------------------- |
| Backend runtime | Python 3.14+, FastAPI, Uvicorn                              |
| ORM / DB        | SQLAlchemy (async), asyncpg, PostgreSQL                     |
| Auth            | bcrypt, python-jose (JWT)                                   |
| Migrations      | Alembic                                                     |
| Realtime        | WebSockets (FastAPI native), Redis pub/sub (Phase 8)        |
| Frontend        | React, TypeScript, Vite, Tailwind, Zustand, React Router    |
| Package manager | `uv` (backend), `npm`/`pnpm` (frontend, not yet scaffolded) |
| Deployment      | Docker Compose, Railway/Render/Fly.io + Vercel              |

## Planned backend structure (from Day 21 refactor phase)

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
