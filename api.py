from fastapi import FastAPI
from auth.controller import router as auth_router
from users.controller import router as user_router
from logs.controller import router as log_router


def register_routes(app: FastAPI):
    app.include_router(auth_router)
    app.include_router(user_router)
    app.include_router(log_router)
