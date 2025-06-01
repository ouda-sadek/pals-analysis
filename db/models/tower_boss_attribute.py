# db/models/tower_boss_attribute.py
from sqlalchemy import Column, Integer, String
from db.base import Base

class TowerBossAttribute(Base):
    __tablename__ = "tower_boss_attribute"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    hp = Column(Integer)
    melee_attack = Column(Integer)
    remote_attack = Column(Integer)
