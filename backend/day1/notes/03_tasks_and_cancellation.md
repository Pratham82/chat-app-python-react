# Notes: 03_tasks_and_cancellation.py

**Date:** 2026-05-09

## Key concepts

- `asyncio.create_task()` schedules a coroutine to run concurrently — it does NOT block. Think of it like `Promise` in JS (fire and forget until you await it).
- Tasks run interleaved: the event loop switches between them at every `await` point (here, `await asyncio.sleep(1)`).
- `task.cancel()` is a regular method (not a coroutine) — it just *requests* cancellation by injecting a `CancelledError` at the next `await`. You must then `await task` to let the task finish its cleanup.
- Re-raising `CancelledError` is mandatory — it signals to asyncio that the task actually completed cancellation. Swallowing it leaves the task in a broken state.

## Gotchas / nuances

- `asyncio.sleep(1)` without `await` does nothing — it creates a coroutine object that is immediately discarded. Always `await` it.
- `await asyncio.create_task(...)` defeats concurrency — it blocks until the task finishes before creating the next one. Just assign the task, don't await the creation.
- `CancelledError` is raised *at the await point* inside the loop, not at the `cancel()` call site. The `except` must wrap the loop, not be inside it.
- Do not `await asyncio.sleep()` inside the `except CancelledError` handler — a second cancellation during cleanup can cause unexpected behavior.
