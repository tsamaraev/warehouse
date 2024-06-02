import models

from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import func


def filter_rolls(
    db: Session,
    id_range: tuple[int, int] = None,
    weight_range: tuple[float, float] = None,
    length_range: tuple[float, float] = None,
    date_added_range: tuple[datetime, datetime] = None,
    date_removed_range: tuple[datetime, datetime] = None,
):
    query = db.query(models.Roll)
    
    if id_range:
        query = query.filter(models.Roll.id.between(id_range[0], id_range[1]))
    if weight_range:
        query = query.filter(models.Roll.weight.between(weight_range[0], weight_range[1]))
    if length_range:
        query = query.filter(models.Roll.length.between(length_range[0], length_range[1]))
    if date_added_range:
        query = query.filter(models.Roll.date_added.between(date_added_range[0], date_added_range[1]))
    if date_removed_range:
        query = query.filter(models.Roll.date_removed.between(date_removed_range[0], date_removed_range[1]))
    
    return query.all()

def get_rolls_statistics(db: Session, start_date: datetime, end_date: datetime):
    query = db.query(models.Roll).filter(models.Roll.date_added.between(start_date, end_date))
    
    total_added = query.count()
    total_removed = db.query(models.Roll).filter(models.Roll.date_removed.between(start_date, end_date)).count()
    
    avg_length = query.with_entities(func.avg(models.Roll.length)).scalar()
    avg_weight = query.with_entities(func.avg(models.Roll.weight)).scalar()
    
    min_length = query.with_entities(func.min(models.Roll.length)).scalar()
    max_length = query.with_entities(func.max(models.Roll.length)).scalar()
    
    min_weight = query.with_entities(func.min(models.Roll.weight)).scalar()
    max_weight = query.with_entities(func.max(models.Roll.weight)).scalar()
    
    total_weight = query.with_entities(func.sum(models.Roll.weight)).scalar()
    
    min_duration = db.query(func.min(func.julianday(models.Roll.date_removed) - func.julianday(models.Roll.date_added))).scalar()
    max_duration = db.query(func.max(func.julianday(models.Roll.date_removed) - func.julianday(models.Roll.date_added))).scalar()
    
    statistics = {
        "total_added": total_added,
        "total_removed": total_removed,
        "avg_length": avg_length,
        "avg_weight": avg_weight,
        "min_length": min_length,
        "max_length": max_length,
        "min_weight": min_weight,
        "max_weight": max_weight,
        "total_weight": total_weight,
        "min_duration": min_duration,
        "max_duration": max_duration
    }
    
    return statistics
