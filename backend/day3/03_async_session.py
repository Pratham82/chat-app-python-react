# DAY 3 — EXERCISE 3: Async SQLAlchemy + FastAPI
#
# TASK: Wire async SQLAlchemy into a FastAPI app using the Depends() pattern.
# This is the exact pattern you'll use in every real route in the chat app.
#
# NOTE: This exercise uses SQLite via aiosqlite for portability.
#       In production (Day 21+) you'll swap DATABASE_URL to:
#       "postgresql+asyncpg://user:pass@localhost/chatdb"
#       and everything else stays the same.
#
# PREREQUISITE: install aiosqlite
#   $ uv add aiosqlite
#
# STEPS:
#   1. Complete get_session() — an async generator that yields an AsyncSession
#      and closes it after the request (use try/finally)
#   2. Implement POST /users — accept CreateUserRequest, insert into DB, return UserOut
#   3. Implement GET /users — return all users
#   4. Implement GET /users/{user_id} — return one user or 404
#   5. Run:
#        $ uv run uvicorn day3.03_async_session:app --reload --port 8000
#   6. Test:
#        $ curl -X POST http://localhost:8000/users \
#            -H "Content-Type: application/json" \
#            -d '{"username":"alice","email":"alice@example.com","password":"secret"}'
#        $ curl http://localhost:8000/users
#        $ curl http://localhost:8000/users/1
#        $ curl http://localhost:8000/users/99
#
# EXPECTED OUTPUT:
#   {"id":1,"username":"alice","email":"alice@example.com"}
#   {"users":[{"id":1,"username":"alice","email":"alice@example.com"}]}
#   {"id":1,"username":"alice","email":"alice@example.com"}
#   {"detail":"User not found"}

import bcrypt
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import String, select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from starlette.status import HTTP_201_CREATED

DATABASE_URL = "sqlite+aiosqlite:///chat_async.db"
engine = create_async_engine(DATABASE_URL)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)

app = FastAPI(title="Chat App API — Day 3")


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)


class CreateUserRequest(BaseModel):
    username: str
    email: str
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    email: str

    model_config = {"from_attributes": True}


async def get_session():
    # TODO: open AsyncSession via SessionLocal(), yield it, close in finally
    async with SessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.post("/users", response_model=UserOut, status_code=HTTP_201_CREATED)
async def create_user(
    body: CreateUserRequest, session: AsyncSession = Depends(get_session)
):
    # TODO: hash password with bcrypt, create User, add, commit, refresh, return
    hashed_password = bcrypt.hashpw(body.password.encode("utf-8"), bcrypt.gensalt())
    new_user = User(
        username=body.username,
        password_hash=hashed_password,
        email=body.email,
    )
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user


@app.get("/users")
async def list_users(session: AsyncSession = Depends(get_session)):
    # TODO: select all users, return {"users": [...]}
    all_users = await session.execute(select(User.id, User.username, User.email))
    return {"users": all_users.mappings().all()}


@app.get("/users/{user_id}", response_model=UserOut)
async def get_user(user_id: int, session: AsyncSession = Depends(get_session)):
    # TODO: get by primary key or raise 404
    user = await session.get(User, user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
