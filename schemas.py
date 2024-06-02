from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class RollBase(BaseModel):
    length: float
    weight: float

class RollCreate(RollBase):
    pass

class Roll(RollBase):
    id: int
    date_added: datetime
    date_removed: Optional[datetime]

    class Config:
        orm_mode = True
