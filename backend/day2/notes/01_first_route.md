# Notes: 01_first_route.py

**Date:** 2026-05-17

## Key concepts

- `FastAPI()` creates the app instance — analogous to `express()` in Node.js; the `title` param shows up in the auto-generated Swagger UI.
- Route decorators (`@app.get("/path")`) map HTTP methods + paths to handler functions — same idea as `app.get('/path', handler)` in Express.
- Returning a plain Python `dict` from a route automatically serializes it to JSON — no `res.json()` needed.
- FastAPI auto-generates interactive docs at `/docs` (Swagger UI) and `/redoc` with zero config.

## Gotchas / nuances

- Handler functions must be `async def` to participate in FastAPI's async event loop; using plain `def` works but blocks the loop.
- The module path for uvicorn uses dot notation (`day2.01_first_route:app`), not a file path — the filename starting with a digit is unusual and can cause import issues in some contexts.
- The `title` kwarg on `FastAPI()` is cosmetic (Swagger UI header only); it doesn't affect routing or validation.
