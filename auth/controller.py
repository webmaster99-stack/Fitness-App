from typing import Annotated
from fastapi import APIRouter, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from database.core import DbSession
from . import schema
from . import service



router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def register_user(db: DbSession, register_user_request: schema.RegisterUserRequest):
    return service.register_user(db, register_user_request)


@router.post("/token", response_model=schema.Token)
async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        db: DbSession
):
    return service.login_for_access_token(form_data, db)
