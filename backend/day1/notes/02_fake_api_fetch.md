# Notes: 02_fake_api_fetch.py

**Date:** 2026-05-09

## Key concepts

- `asyncio.gather(*coroutines)` runs multiple coroutines concurrently and waits for all to finish — equivalent to `Promise.all()` in JS
- Total elapsed time ≈ the slowest single coroutine, not the sum of all delays — this is the core benefit of concurrency
- Unpack a list of coroutines into `gather()` with the splat operator: `gather(*[notify_user(uid) for uid in user_ids])`
- `gather()` returns a list of results in the same order as the input coroutines, regardless of completion order

## Gotchas / nuances

- Shadowing the parameter inside the function (`user_ids = [1,2,3,4]`) silently breaks the function for any other input — always use the parameter as-is
- Print statements fire in completion order (non-deterministic), but `gather()` return values are always in input order
- `random.uniform(a, b)` — easy to pass wrong bounds; double-check the range matches the spec
- `time.perf_counter()` is preferred over `time.time()` for measuring short durations — higher resolution
