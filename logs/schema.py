from pydantic import BaseModel, Field
from uuid import UUID
from enum import StrEnum
from datetime import datetime


class MealType(StrEnum):
    BREAKFAST = "breakfast"
    LUNCH = "lunch"
    DINNER = "dinner"
    SNACK = "snack"
    OTHER = "other"


class CalorieLogBase(BaseModel):
    food_name: str
    quantity: int = Field(gt=0)
    calories_per_100g: int = Field(gt=0)


class CalorieLogCreate(CalorieLogBase):
    meal_type: MealType = Field(default=MealType.OTHER)


class CalorieLogResponse(CalorieLogBase):
    id: UUID
    user_id: UUID
    total_calories: int
    meal_type: MealType = Field(default=MealType.OTHER)
    log_date: datetime

    class Config:
        orm_mode = True


class CalorieLogUpdate(CalorieLogBase):
    food_name: str | None = None
    quantity: int | None = None
    calories_per_100g: int | None = None
