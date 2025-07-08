from fastapi import APIRouter, status
from . import schema
from . import service
from auth.service import CurrentUser
from database.core import DbSession


router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me", response_model=schema.UserResponse)
def get_current_user(current_user: CurrentUser, db: DbSession):
    return service.get_user_by_id(db, current_user.get_uuid())


@router.put("/change-password", status_code=status.HTTP_200_OK)
def change_password(
    password_change: schema.PasswordChange,
    db: DbSession,
    current_user: CurrentUser
):
    return service.change_password(db, current_user.get_uuid(), password_change)


@router.put("/set-goal", status_code=status.HTTP_200_OK)
def set_daily_goal(
        db: DbSession,
        current_user: CurrentUser,
        daily_goal: schema.SetDailyGoal
):
    return  service.set_daily_goal(db, current_user.get_uuid(), daily_goal)