from sqlalchemy import Column, Integer, Float, DateTime
from database import Base
from datetime import datetime

class Roll(Base):
    __tablename__ = "rolls"

    id = Column(Integer, primary_key=True, index=True)
    length = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)
    date_added = Column(DateTime, default=datetime.utcnow)
    date_removed = Column(DateTime, nullable=True)
