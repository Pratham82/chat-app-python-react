# DAY 2 — EXERCISE 4: Dependency Injection
#
# TASK: FastAPI's Depends() lets you extract shared logic (DB sessions, auth,
# pagination) into reusable functions injected into route handlers.
# This is the pattern you'll use for every real route in the chat app.
#
# STEPS:
#   1. Implement get_db() — a fake "DB session" dependency that prints
#      "opening DB connection" on entry and "closing DB connection" on exit
#      (use yield so cleanup runs after the response is sent)
#   2. Implement pagination() — parses `page` and `page_size` query params
#      and returns {"offset": ..., "limit": ...}
#   3. Implement get_current_user() — reads an `x-user-id` header; if missing
#      or not a valid int, raise HTTPException(401, "missing or invalid x-user-id")
#   4. Wire all three into list_messages():
#      - requires auth (get_current_user)
#      - uses pagination (pagination)
#      - uses db (get_db)
#      - returns a slice of MESSAGES using offset/limit, plus who's asking
#   5. Run:
#        $ uv run uvicorn day2.04_dependency_injection:app --reload --port 8000
#   6. Test:
#        $ curl "http://localhost:8000/messages" -H "x-user-id: 1"
#        $ curl "http://localhost:8000/messages?page=2&page_size=2" -H "x-user-id: 1"
#        $ curl "http://localhost:8000/messages"   # missing header → 401
#
# EXPECTED OUTPUT:
#   {"requested_by":1,"page":1,"messages":[{"id":1,...},{"id":2,...},{"id":3,...},{"id":4,...},{"id":5,...}]}
#   {"requested_by":1,"page":2,"messages":[{"id":3,"text":"hey Charlie!","from_id":2},{"id":4,...}]}
#   {"detail":"missing or invalid x-user-id"}

from fastapi import Depends, FastAPI, Header, HTTPException

app = FastAPI(title="Chat App API")

MESSAGES = [
    {"id": 1, "text": "hello!", "from_id": 1},
    {"id": 2, "text": "hey Alice", "from_id": 2},
    {"id": 3, "text": "hey Charlie!", "from_id": 2},
    {"id": 4, "text": "what's up", "from_id": 3},
    {"id": 5, "text": "not much", "from_id": 1},
    {"id": 6, "text": "cool cool", "from_id": 3},
]


async def get_db():
    # TODO: print "opening DB connection", yield a fake db object (e.g. {}),
    # then print "closing DB connection" in a finally block
    yield {}


def pagination(page: int = 1, page_size: int = 5) -> dict:
    # TODO: return {"offset": (page - 1) * page_size, "limit": page_size, "page": page}
    pass


async def get_current_user(x_user_id: str | None = Header(default=None)) -> int:
    # TODO: if x_user_id is None or not a digit, raise 401
    # otherwise return int(x_user_id)
    pass


@app.get("/messages")
async def list_messages(
    user_id: int = Depends(get_current_user),
    pages: dict = Depends(pagination),
    db: dict = Depends(get_db),
):
    # TODO: slice MESSAGES[offset : offset + limit], return with requested_by and page
    pass
