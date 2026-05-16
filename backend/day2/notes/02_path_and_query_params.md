# Notes: 02_path_and_query_params.py

**Date:** 2026-05-17

## Key concepts

- **Path params** are declared in the route string as `{param}` and matched as function arguments — FastAPI auto-validates and coerces the type (e.g. `/users/{user_id}` with `user_id: int` rejects non-integers with a 422).
- **Query params** are any function arguments not in the route string — `online: bool | None = None` becomes `?online=true/false`, and FastAPI parses the string `"true"` into Python `True` automatically.
- Raise `HTTPException(status_code=404, detail="...")` to return error responses; FastAPI serializes it to `{"detail": "..."}`.
- Route order matters: more specific routes (e.g. `/users/me`) must be declared _before_ parameterized ones (`/users/{user_id}`) or FastAPI will match the param route first.

## Gotchas / nuances

- **Generator expression with `next()`**: `next((u for u in USERS if u["id"] == user_id), None)` is the idiomatic way to find the first match in a list without importing anything. The second argument to `next()` is the default if the iterator is exhausted — omitting it raises `StopIteration` instead of returning `None`.
- Generator expressions are lazy — they don't build a list in memory, they yield one item at a time. Combined with `next()`, iteration stops at the first match (short-circuit), which is more efficient than a list comprehension that scans everything.
- `bool | None = None` requires Python 3.10+; the older equivalent is `Optional[bool] = None` from `typing`.
- Slicing `[:limit]` on a list always works even if `limit` exceeds the list length — no index error.
