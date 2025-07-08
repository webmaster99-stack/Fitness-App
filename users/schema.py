from uuid import UUID
from pydantic import BaseModel, EmailStr, Field


class UserResponse(BaseModel):
    id: UUID
    username: str
    email: EmailStr


class PasswordChange(BaseModel):
    current_password: str
    new_password: str
    new_password_confirm: str


class SetDailyGoal(BaseModel):
    daily_goal: int = Field(gt=0)
