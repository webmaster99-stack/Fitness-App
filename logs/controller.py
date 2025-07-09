from uuid import UUID
from fastapi import APIRouter, status
from auth.service import CurrentUser
from database.core import DbSession
from . import service
from . import schema

router = APIRouter(prefix="/logs", tags=["Calorie Logs"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.CalorieLogResponse)
async def create_log(
        db: DbSession,
        current_user: CurrentUser,
        request: schema.CalorieLogCreate
):
    return service.create_log(db, current_user.get_uuid(), request)


@router.get("/", response_model=list[schema.CalorieLogResponse])
async def get_logs(db: DbSession, current_user: CurrentUser):
    return service.get_logs(db, current_user.get_uuid())


@router.get("/{log_id}", response_model=schema.CalorieLogResponse)
async def get_log(db: DbSession, current_user: CurrentUser, log_id: UUID):
    return service.get_log(db, current_user.get_uuid(), log_id)


@router.put("/{log_id}", response_model=schema.CalorieLogResponse)
async def update_log(
        db: DbSession,
        current_user: CurrentUser,
        log_id: UUID,
        log_update: schema.CalorieLogUpdate
):
    return service.update_log(db, current_user.get_uuid(), log_id, log_update)


@router.delete("/{log_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_log(db: DbSession, current_user: CurrentUser, log_id: UUID):
    return service.delete_log(db, current_user.get_uuid(), log_id)
