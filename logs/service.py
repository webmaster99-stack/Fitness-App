from fastapi import HTTPException, status
from uuid import UUID
from sqlalchemy.orm import Session
from logs.schema import CalorieLogCreate, CalorieLogUpdate
from models import CalorieLog


def calculate_total_calories(calories_per_100g: int, quantity: int) -> int:
    return round((quantity / 100) * calories_per_100g)


def create_log(db: Session, user_id: UUID, request: CalorieLogCreate) -> CalorieLog:
    try:
        new_log = CalorieLog(request.model_dump())
        new_log.user_id = user_id
        new_log.total_calories = calculate_total_calories(request.calories_per_100g, request.quantity)

        db.add(new_log)
        db.commit()
        db.refresh(new_log)

        return new_log

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create a calorie log. Error {str(e)}"
        )


def get_logs(db: Session, user_id: UUID) -> list[type[CalorieLog]]:
    logs = db.query(CalorieLog).filter(CalorieLog.user_id == user_id).all()
    return logs


def get_log(db: Session, user_id: UUID, log_id: UUID) -> type[CalorieLog]:
    log = db.query(CalorieLog).filter(
        CalorieLog.user_id == user_id
    ).filter(CalorieLog.id == log_id).first()

    if not log:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Calorie log not found"
        )

    return log


def update_log(
        db: Session,
        user_id: UUID,
        log_id: UUID,
        log_update: CalorieLogUpdate
) -> type[CalorieLog]:
    log_data = log_update.model_dump(exclude_unset=True)

    db.query(CalorieLog).filter(
        CalorieLog.id == log_id
    ).filter(CalorieLog.user_id == user_id).update(log_data)
    db.commit()

    return get_log(db, user_id, log_id)


def delete_log(db: Session, user_id: UUID, log_id: UUID) -> None:
    log = get_log(db, user_id, log_id)
    db.delete(log)
    db.commit()