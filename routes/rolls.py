import crud
import models
import schemas

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional, Tuple
from datetime import datetime
from database import SessionLocal, engine
from utils import filter_rolls, get_rolls_statistics


router = APIRouter()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/rolls/", response_model=schemas.Roll)
def create_roll(roll: schemas.RollCreate, db: Session = Depends(get_db)):
    return crud.create_roll(db=db, roll=roll)

@router.delete("/rolls/{roll_id}", response_model=schemas.Roll)
def delete_roll(roll_id: int, db: Session = Depends(get_db)):
    db_roll = crud.delete_roll(db=db, roll_id=roll_id)
    if db_roll is None:
        raise HTTPException(status_code=404, detail="Roll not found")
    return db_roll

@router.get("/rolls/", response_model=list[schemas.Roll])
def read_rolls(
    id_range: Optional[Tuple[int, int]] = Query(None),
    weight_range: Optional[Tuple[float, float]] = Query(None),
    length_range: Optional[Tuple[float, float]] = Query(None),
    date_added_range: Optional[Tuple[datetime, datetime]] = Query(None),
    date_removed_range: Optional[Tuple[datetime, datetime]] = Query(None),
    db: Session = Depends(get_db)
):
    rolls = filter_rolls(
        db=db,
        id_range=id_range,
        weight_range=weight_range,
        length_range=length_range,
        date_added_range=date_added_range,
        date_removed_range=date_removed_range
    )
    return rolls

@router.get("/rolls/statistics/", response_model=dict)
def rolls_statistics(start_date: datetime, end_date: datetime, db: Session = Depends(get_db)):
    return get_rolls_statistics(db=db, start_date=start_date, end_date=end_date)
