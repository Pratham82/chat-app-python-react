# DAY 4 — EXERCISE 3: Signup & Login Routes
#
# TASK: Build the two auth endpoints. Signup creates an account;
# login validates credentials and returns a JWT.
#
# STEPS:
#   1. Implement POST /signup:
#      - reject if username already exists (409 Conflict)
#      - hash the password, store user in USERS, return UserOut
#   2. Implement POST /login:
#      - find user by username; if not found → 401
#      - verify password; if wrong → 401 (same message — don't leak which failed)
#      - return {"access_token": <jwt>, "token_type": "bearer"}
#   3. Run:
#        $ uv run uvicorn day4.03_auth_routes:app --reload --port 8000
#   4. Test:
#        $ curl -X POST http://localhost:8000/signup \
#            -H "Content-Type: application/json" \
#            -d '{"username":"alice","email":"alice@example.com","password":"secret123"}'
#
#        $ curl -X POST http://localhost:8000/login \
#            -H "Content-Type: application/json" \
#            -d '{"username":"alice","password":"secret123"}'
#
#        $ curl -X POST http://localhost:8000/login \
#            -H "Content-Type: application/json" \
#            -d '{"username":"alice","password":"wrongpass"}'
#
# EXPECTED OUTPUT:
#   {"id":1,"username":"alice","email":"alice@example.com"}
#   {"access_token":"eyJ...","token_type":"bearer"}
#   {"detail":"Invalid credentials"}

from datetime import timedelta

import bcrypt
from fastapi import FastAPI, HTTPException
from jose import jwt
from pydantic import BaseModel
from starlette.status import HTTP_201_CREATED, HTTP_409_CONFLICT

SECRET_KEY = "dev-secret-do-not-use-in-prod"
ALGORITHM = "HS256"

app = FastAPI(title="Chat App API — Auth")

USERS: list[dict] = []
_next_id = 1


class SignupRequest(BaseModel):
    username: str
    email: str
    password: str


class LoginRequest(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    email: str


def _find_user(username: str) -> dict | None:
    return next((u for u in USERS if u["username"] == username), None)


def _create_token(user_id: int) -> str:
    from datetime import UTC, datetime
    payload = {
        "sub": user_id,
        "exp": datetime.now(UTC) + timedelta(hours=1),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


@app.post("/signup", response_model=UserOut, status_code=HTTP_201_CREATED)
async def signup(body: SignupRequest):
    global _next_id
    # TODO: check duplicate username → 409
    # TODO: hash password, build user dict, append to USERS, return UserOut
    pass


@app.post("/login")
async def login(body: LoginRequest):
    # TODO: find user → 401 if not found
    # TODO: verify password → 401 if wrong (same "Invalid credentials" message)
    # TODO: return {"access_token": ..., "token_type": "bearer"}
    pass
