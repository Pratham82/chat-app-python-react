# Notes: 03_request_body_and_models.py

**Date:** 2026-05-17

## Key concepts

- Pydantic `BaseModel` defines both request bodies and response shapes — FastAPI auto-validates incoming JSON and serializes outgoing data based on these models.
- Declaring a parameter with a `BaseModel` type in a route function signals FastAPI to parse it from the request body (not the path or query string).
- `response_model=UserResponse` on the decorator filters the return value — only fields declared in the model are included in the response, even if you return a dict with extra keys.
- `status_code=HTTP_201_CREATED` sets the default success status; importing from `starlette.status` is idiomatic over using bare integers.

## Gotchas / nuances

- Optional fields need an explicit default: `online: bool = False` — without the default, Pydantic treats the field as required and rejects requests that omit it.
- You cannot pass a plain `dict` as a positional arg to a Pydantic model: `UserResponse(user)` fails. Use `UserResponse(**user)` to unpack the dict into keyword arguments.
- FastAPI returns a 422 (not 400) for validation errors — the response body includes a structured `detail` list with `type`, `loc`, and `msg` for each failed field.
- `create_user` doesn't need to explicitly set `status_code=201` in the return — the status code is declared on the decorator and applied automatically.
