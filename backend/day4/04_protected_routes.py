# DAY 4 — EXERCISE 4: Protected Routes with JWT
#
# TASK: Add GET /me — a route only accessible with a valid JWT.
# The token is passed in the Authorization header as "Bearer <token>".
# Extract and validate it in a dependency so any route can require auth
# with a single Depends(get_current_user).
#
# STEPS:
#   1. Implement get_current_user():
#      - read the Authorization header
#      - expect format "Bearer <token>"; raise 401 if missing or malformed
#      - decode the token; raise 401 if invalid or expired
#      - look up the user by id from payload["sub"]; raise 401 if not found
#      - return the user dict
#   2. GET /me is already wired — just make sure get_current_user works
#   3. Run:
#        $ uv run uvicorn day4.04_protected_routes:app --reload --port 8000
#   4. Test:
#        # signup first:
#        $ curl -X POST http://localhost:8000/signup \
#            -H "Content-Type: application/json" \
#            -d '{"username":"alice","email":"alice@example.com","password":"secret123"}'
#
#        # login to get token:
#        $ TOKEN=$(curl -s -X POST http://localhost:8000/login \
#            -H "Content-Type: application/json" \
#            -d '{"username":"alice","password":"secret123"}' | python3 -c "import sys,json; print(json.load(sys.stdin)['access_token'])")
#
#        # hit protected route:
#        $ curl http://localhost:8000/me -H "Authorization: Bearer $TOKEN"
#
#        # no token:
#        $ curl http://localhost:8000/me
#
# EXPECTED OUTPUT:
#   {"id":1,"username":"alice","email":"alice@example.com"}
#   {"detail":"Not authenticated"}

from datetime import UTC, datetime, timedelta

import bcrypt
from fastapi import Depends, FastAPI, HTTPException, Header
from jose import JWTError, jwt
from pydantic import BaseModel
from starlette.status import HTTP_201_CREATED, HTTP_401_UNAUTHORIZED

SECRET_KEY = "dev-secret-do-not-use-in-prod"
ALGORITHM = "HS256"

app = FastAPI(title="Chat App API — Protected Routes")

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


def _make_token(user_id: int) -> str:
    payload = {"sub": user_id, "exp": datetime.now(UTC) + timedelta(hours=1)}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(authorization: str | None = Header(default=None)) -> dict:
    credentials_error = HTTPException(
        status_code=HTTP_401_UNAUTHORIZED,
        detail="Not authenticated",
        headers={"WWW-Authenticate": "Bearer"},
    )
    # TODO: check authorization is not None and starts with "Bearer "
    # TODO: extract token, decode it (catch JWTError → raise credentials_error)
    # TODO: get sub from payload, find user in USERS → raise credentials_error if not found
    # TODO: return user dict


@app.post("/signup", response_model=UserOut, status_code=HTTP_201_CREATED)
async def signup(body: SignupRequest):
    global _next_id
    pw_hash = bcrypt.hashpw(body.password.encode(), bcrypt.gensalt()).decode()
    user = {"id": _next_id, "username": body.username, "email": body.email, "password_hash": pw_hash}
    USERS.append(user)
    _next_id += 1
    return user


@app.post("/login")
async def login(body: LoginRequest):
    user = next((u for u in USERS if u["username"] == body.username), None)
    if not user or not bcrypt.checkpw(body.password.encode(), user["password_hash"].encode()):
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return {"access_token": _make_token(user["id"]), "token_type": "bearer"}


@app.get("/me", response_model=UserOut)
async def me(current_user: dict = Depends(get_current_user)):
    return current_user
