# DAY 2 — EXERCISE 2: Path Params & Query Params
#
# TASK: Add user-lookup routes. FastAPI extracts path params from the URL
# and query params from the query string — both are type-validated automatically.
#
# STEPS:
#   1. Implement get_user_by_id():
#      - path param: user_id (int)
#      - look it up in USERS; if not found raise HTTPException(404)
#      - return the user dict
#   2. Implement list_users():
#      - query param: online (bool, optional, default None) — filter by online status
#      - query param: limit (int, optional, default 10) — max results to return
#      - return {"users": [...], "count": N}
#   3. Run:
#        $ uv run uvicorn day2.02_path_and_query_params:app --reload --port 8000
#   4. Test:
#        $ curl "http://localhost:8000/users"
#        $ curl "http://localhost:8000/users?online=true"
#        $ curl "http://localhost:8000/users?online=false&limit=1"
#        $ curl "http://localhost:8000/users/1"
#        $ curl "http://localhost:8000/users/99"
#
# EXPECTED OUTPUT:
#   {"users":[{"id":1,"name":"Alice","online":true},{"id":2,"name":"Bob","online":false},{"id":3,"name":"Charlie","online":true}],"count":3}
#   {"users":[{"id":1,"name":"Alice","online":true},{"id":3,"name":"Charlie","online":true}],"count":2}
#   {"users":[{"id":2,"name":"Bob","online":false}],"count":1}
#   {"id":1,"name":"Alice","online":true}
#   {"detail":"User not found"}

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Chat App API")

USERS = [
    {"id": 1, "name": "Alice", "online": True},
    {"id": 2, "name": "Bob", "online": False},
    {"id": 3, "name": "Charlie", "online": True},
]


class User(BaseModel):
    id: int
    name: str
    online: bool


@app.get("/users/{user_id}")
async def get_user_by_id(user_id: int) -> User:
    user = next((u for u in USERS if u["id"] == user_id), None)
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")


@app.get("/users")
async def list_users(online: bool | None = None, limit: int = 10):
    result = (USERS if online is None else [u for u in USERS if u["online"] == online])[
        :limit
    ]

    return {"users": result, "count": len(result)}
