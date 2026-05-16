# DAY 2 — EXERCISE 3: Request Body + Pydantic Models
#
# TASK: Add POST /users to create a new user. Pydantic models define the shape
# of request bodies and responses — FastAPI validates and (de)serializes them.
#
# STEPS:
#   1. Fill in the CreateUserRequest model:
#      - name: str (required)
#      - email: str (required)
#      - online: bool (optional, default False)
#   2. Implement create_user():
#      - generate a new id (len(USERS) + 1)
#      - append the new user dict to USERS
#      - return a UserResponse with status_code 201
#   3. Implement get_user():
#      - same as exercise 2 — return UserResponse or 404
#   4. Run:
#        $ uv run uvicorn day2.03_request_body_and_models:app --reload --port 8000
#   5. Test:
#        $ curl -X POST http://localhost:8000/users \
#            -H "Content-Type: application/json" \
#            -d '{"name":"Diana","email":"diana@example.com"}'
#        $ curl http://localhost:8000/users/4
#        $ curl -X POST http://localhost:8000/users \
#            -H "Content-Type: application/json" \
#            -d '{"name":"Eve"}'    # missing email — should return 422
#
# EXPECTED OUTPUT:
#   {"id":4,"name":"Diana","email":"diana@example.com","online":false}
#   {"id":4,"name":"Diana","email":"diana@example.com","online":false}
#   {"detail":[{"type":"missing","loc":["body","email"],...}]}  ← 422 Unprocessable Entity


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from starlette.status import HTTP_201_CREATED

app = FastAPI(title="Chat App API")

USERS: list[dict] = [
    {"id": 1, "name": "Alice", "email": "alice@example.com", "online": True},
    {"id": 2, "name": "Bob", "email": "bob@example.com", "online": False},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com", "online": True},
]


class CreateUserRequest(BaseModel):
    # TODO: define fields: name (str), email (str), online (bool = False)
    name: str
    email: str
    online: bool = False


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    online: bool


@app.post("/users", response_model=UserResponse, status_code=HTTP_201_CREATED)
async def create_user(body: CreateUserRequest):
    new_user = {
        "id": len(USERS) + 1,
        "name": body.name,
        "email": body.email,
        "online": body.online,
    }

    USERS.append(new_user)

    return UserResponse(**new_user)


@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    user = next((u for u in USERS if u["id"] == user_id), None)

    if user:
        return UserResponse(**user)
    else:
        raise HTTPException(404)
