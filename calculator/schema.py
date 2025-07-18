from pydantic import BaseModel, Field
from enum import StrEnum


class SexChoices(StrEnum):
    MALE = "male"
    FEMALE = "female"


class UserData(BaseModel):
    weigh: float = Field(gt=0)
    height: float = Field(gt=0)
    sex: SexChoices = Field(default=SexChoices.MALE)
    age: int = Field(gt=0, le=100)


class BMRBase(BaseModel):
    bmr: int = Field(gt=0)


class BMRResponse(BMRBase):
    pass


class BMRRequest(BMRBase):
    pass
