# DAY 4 — EXERCISE 2: JWT Tokens
#
# TASK: After login, the server issues a JWT (JSON Web Token) — a signed
# payload the client sends back on every request to prove their identity.
# The server verifies the signature without hitting the DB.
#
# STEPS:
#   1. Implement create_access_token():
#      - build payload: {"sub": user_id, "exp": now + expires_delta}
#      - sign with SECRET_KEY and HS256 algorithm
#      - return the token string
#   2. Implement decode_token():
#      - decode and verify the token
#      - return the payload dict
#      - raise ValueError with a descriptive message on any JWTError
#   3. Run:
#        $ uv run python day4/02_jwt_tokens.py
#
# EXPECTED OUTPUT:
#   Token: eyJ...   (long JWT string)
#   Decoded payload: {'sub': 42, 'exp': <timestamp>}
#   User ID from token: 42
#   Expired token error: <some expiry error message>
#   Tampered token error: <some signature error message>

from datetime import UTC, datetime, timedelta

from jose import JWTError, jwt

SECRET_KEY = "dev-secret-do-not-use-in-prod"
ALGORITHM = "HS256"


def create_access_token(user_id: int, expires_delta: timedelta = timedelta(hours=1)) -> str:
    # TODO: build payload with "sub" and "exp", return jwt.encode(...)
    pass


def decode_token(token: str) -> dict:
    # TODO: jwt.decode(...), catch JWTError and raise ValueError
    pass


if __name__ == "__main__":
    token = create_access_token(user_id=42)
    print(f"Token: {token}")

    payload = decode_token(token)
    print(f"Decoded payload: {{'sub': {payload['sub']}, 'exp': {payload['exp']}}}")
    print(f"User ID from token: {payload['sub']}")

    # expired token
    expired = create_access_token(user_id=1, expires_delta=timedelta(seconds=-1))
    try:
        decode_token(expired)
    except ValueError as e:
        print(f"Expired token error: {e}")

    # tampered token
    try:
        decode_token(token + "tampered")
    except ValueError as e:
        print(f"Tampered token error: {e}")
