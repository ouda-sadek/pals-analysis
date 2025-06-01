# db/models/refresh_area.py
from sqlalchemy import Column, Integer, String
from db.base import Base

class RefreshArea(Base):
    __tablename__ = "refresh_area"

    id = Column(Integer, primary_key=True, autoincrement=True)
    pal_name = Column(String(255))
    min_level = Column(Integer)
    max_level = Column(Integer)
    area = Column(String(255))

