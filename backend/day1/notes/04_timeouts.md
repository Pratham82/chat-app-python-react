# Notes: 04_timeouts.py

**Date:** 2026-05-09

## Key concepts

- `asyncio.wait_for(coro, timeout=N)` wraps any coroutine with a deadline — analogous to `Promise.race([coro, sleep(N)])` in JS but built-in
- If the coroutine exceeds the timeout, it is **cancelled** and `asyncio.TimeoutError` (aliased as `TimeoutError` in Python 3.11+) is raised
- This is the standard pattern for protecting I/O-bound operations (DB writes, HTTP calls, etc.) from hanging indefinitely — critical in a chat backend where slow DB ops shouldn't stall WebSocket handlers

## Gotchas / nuances

- `asyncio.wait_for()` cancels the underlying task on timeout — the coroutine doesn't just stop being awaited, it receives a `CancelledError` internally; any cleanup in the coroutine (e.g. `finally` blocks) will still run
- In Python 3.11+ `TimeoutError` is the built-in; in older versions you had to catch `asyncio.TimeoutError` — they're now the same class but older code may use the namespaced form
- The timeout clock starts when `wait_for` is awaited, not when the coroutine is created — so wrapping a pre-started coroutine doesn't reset the timer
