# DAY 2 — EXERCISE 1: Your First FastAPI Routes
#
# TASK: Start building the chat app's backend API.
# FastAPI automatically generates docs, validates types, and serializes JSON.
#
# STEPS:
#   1. Read the two routes below and understand what they do.
#   2. Add a third route: GET /version → return {"version": "0.1.0", "name": "chat-app"}
#   3. Run the server:
#        $ uv run uvicorn day2.01_first_route:app --reload --port 8000
#   4. Open http://localhost:8000/docs — explore the auto-generated Swagger UI
#   5. Hit each route:
#        $ curl http://localhost:8000/health
#        $ curl http://localhost:8000/info
#        $ curl http://localhost:8000/version
#
# EXPECTED OUTPUT (curl responses):
#   {"status":"ok"}
#   {"message":"Chat app API","docs":"/docs"}
#   {"version":"0.1.0","name":"chat-app"}

from fastapi import FastAPI

app = FastAPI(title="Chat App API")


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/info")
async def info():
    return {"message": "Chat app API", "docs": "/docs"}


# TODO: add GET /version here
@app.get("/version")
async def version():
    return {"version": "0.1.0", "name": "chat-app"}
