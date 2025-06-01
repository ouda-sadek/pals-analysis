# db/models/ordinary_boss_attribute.py
from sqlalchemy import Column, Integer, String
from db.base import Base

class OrdinaryBossAttribute(Base):
    __tablename__ = "ordinary_boss_attribute"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    hp = Column(Integer)
    attack = Column(Integer)
    defense = Column(Integer)
    speed = Column(Integer)
