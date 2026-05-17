# Notes: 04_dependency_injection.py

**Date:** 2026-05-17

## Key concepts

- `Depends(fn)` tells FastAPI to run `fn` before the route handler and inject its return value as an argument — you never call the dependency yourself.
- Dependencies are composable: a route can declare multiple `Depends()` parameters, each resolved independently (similar to middleware in Express, but per-parameter and reusable across routes).
- Generator dependencies (`yield`-based like `get_db`) split into setup and teardown: code before `yield` runs before the response, code in `finally` runs after — same pattern as Python context managers (`with` statement).
- `Header(default=None)` maps a snake_case parameter name to a kebab-case HTTP header automatically (`x_user_id` → `x-user-id`).

## Gotchas / nuances

- If a dependency raises `HTTPException`, FastAPI short-circuits immediately — the route handler never runs. So after a successful `Depends(get_current_user)`, the user is always authenticated; an `if user_id` guard in the body is redundant.
- `get_db` uses `yield` inside a `try/finally` — if you use a plain `return {}` instead, the cleanup code never executes (connection never "closed"). Always `yield` + `finally` for cleanup.
- `pagination`'s default `page=1, page_size=5` are query param defaults, not function defaults in the normal sense — FastAPI reads them from the request URL, falling back to these values if absent.
- The `else: print()` branch in the original stub is dead code: `get_current_user` either returns a truthy int or raises, so the `else` arm is unreachable.
