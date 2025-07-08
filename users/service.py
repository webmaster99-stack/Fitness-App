from uuid import UUID
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from . import schema
from models import User
from auth.service import verify_password, get_password_hash


def get_user_by_id(db: Session, user_id: UUID) -> schema.UserResponse:
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user


def change_password(
        db: Session,
        user_id: UUID,
        password_change: schema.PasswordChange
) -> None:
    try:
        user = get_user_by_id(db, user_id)

        if not verify_password(password_change.current_password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid current password provided for user ID: {user_id}"
            )

        if password_change.new_password != password_change.new_password_confirm:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Password mismatch during change attempt for user ID: {user_id}"
            )

        user.hashed_password = get_password_hash(password_change.new_password)
        db.commit()

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error during password change for user ID: {user_id}. Error: {str(e)}"
        )


def set_daily_goal(db: Session, user_id: UUID, daily_goal: schema.SetDailyGoal) -> None:
    try:
        user = get_user_by_id(db, user_id)

        user.daily_goal = daily_goal.daily_goal
        db.commit()

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Updating daily goal failed. Error {str(e)}"
        )
