from uuid import UUID
from calculator.schema import UserData, BMRResponse, BMRRequest


def calculate_bmr(user_id: UUID, request: UserData) -> BMRResponse:
    if request.sex == "male":
        bmr = 66 + (6.3 * request.weight) + (12.9 * request.height) - (6.8 * request.age)
    else:
        bmr = 655 + (4.3 * request.weight) + (4.7 * request.height) - (4.7 * request.age)
    return round(bmr)


def calculate_daily_calories(
        bmr_request: BMRRequest,
        user_id: UUID,
        activity_level: str
) -> int:
    levels = {
        "sedentary": 1.2,
        "lightly active": 1.375,
        "moderately active": 1.55,
        "very active": 1.725
    }

    return round(bmr_request.bmr * levels.get(activity_level, 1.2))