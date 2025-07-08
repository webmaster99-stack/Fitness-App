from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from database.core import Base
from datetime import datetime, timezone
from uuid import uuid4


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    daily_goal = Column(Integer, default=0)
    is_admin = Column(Boolean, default=False)
    logs = relationship("CalorieLog", back_populates="user")


class CalorieLog(Base):
    __tablename__ = "logs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    food_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    calories_per_100g = Column(Integer, nullable=False)
    total_calories = Column(Integer, nullable=False)
    meal_type = Column(String, nullable=False)
    log_date = Column(DateTime, nullable=False, default=datetime.now(timezone.utc))
