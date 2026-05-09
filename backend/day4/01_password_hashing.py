# DAY 4 — EXERCISE 1: Password Hashing with bcrypt
#
# TASK: Passwords must NEVER be stored in plain text. bcrypt hashes a password
# into a one-way digest — you can verify a guess against it, but can't reverse it.
#
# STEPS:
#   1. Implement hash_password() — return a bcrypt hash of the plain-text password
#   2. Implement verify_password() — return True if plain matches the stored hash
#   3. Run:
#        $ uv run python day4/01_password_hashing.py
#
# EXPECTED OUTPUT:
#   Hash: $2b$12$...   (60-char bcrypt string, different every run)
#   Correct password: True
#   Wrong password:   False
#   Two hashes of same password are different: True
#   But both verify: True

import bcrypt


def hash_password(plain: str) -> str:
    # TODO: bcrypt.hashpw needs bytes — encode plain, hash it, decode result to str
    pass


def verify_password(plain: str, hashed: str) -> bool:
    # TODO: bcrypt.checkpw — encode both sides, return result
    pass


if __name__ == "__main__":
    password = "supersecret123"

    h1 = hash_password(password)
    h2 = hash_password(password)

    print(f"Hash: {h1}")
    print(f"Correct password: {verify_password(password, h1)}")
    print(f"Wrong password:   {verify_password('wrongpass', h1)}")
    print(f"Two hashes of same password are different: {h1 != h2}")
    print(f"But both verify: {verify_password(password, h2)}")
