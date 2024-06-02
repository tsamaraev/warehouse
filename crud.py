import models
import schemas

from sqlalchemy.orm import Session
from datetime import datetime

def get_rolls(db: Session):
    return db.query(models.Roll).all()

def create_roll(db: Session, roll: schemas.RollCreate):
    db_roll = models.Roll(length=roll.length, weight=roll.weight)
    db.add(db_roll)
    db.commit()
    db.refresh(db_roll)
    return db_roll

def delete_roll(db: Session, roll_id: int):
    db_roll = db.query(models.Roll).filter(models.Roll.id == roll_id).first()
    if db_roll:
        db_roll.date_removed = datetime.utcnow()
        db.commit()
        db.refresh(db_roll)
    return db_roll
