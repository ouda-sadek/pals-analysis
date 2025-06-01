# db/models/job_skill.py
from sqlalchemy import Column, Integer, String, Float
from db.base import Base

class JobSkill(Base):
    __tablename__ = "job_skill"

    id = Column(Integer, primary_key=True, autoincrement=True)
    english_name = Column(String(255))
    chinese_name = Column(String(255))
    volume_size = Column(String(100))
    food_intake = Column(Integer)
    night_shift = Column(String(50))
    total_skills = Column(Integer)
    make_fire = Column(Integer)
    watering = Column(Integer)
    planting = Column(Integer)
    logging = Column(Integer)
    mining = Column(Integer)
    pharmaceutical = Column(Integer)
    cool_down = Column(Integer)
    pasture = Column(Integer)
    carry = Column(Integer)
    handling_speed = Column(Float)
    ranch_items = Column(String(255))
    pasture_output = Column(Integer)
    ranch_size_rank = Column(String(50))

