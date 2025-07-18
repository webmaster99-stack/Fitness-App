from fastapi import APIRouter
from auth.service import CurrentUser
from . import schema
from . import service


router = APIRouter(
    prefix="/calculator",
    tags=["Calculator"]
)


@router.get("/bmr", response_model=schema.BMRResponse)
async def calculate_bmr(current_user: CurrentUser, request: schema.UserData):
    return service.calculate_bmr(current_user.get_uuid(), request)


@router.get("/daily-intake")
async def calculate_daily_calories(
        request: schema.BMRRequest,
        current_user: CurrentUser,
        activity_level: str
):
    return service.calculate_daily_calories(request, current_user.get_uuid(), activity_level)