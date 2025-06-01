# db/models/combat_attribute.py
from sqlalchemy import Column, Integer, String, Float, Boolean
from db.base import Base

class CombatAttribute(Base):
    __tablename__ = "combat_attribute"

    id = Column(Integer, primary_key=True, autoincrement=True)
    chinese_name = Column(String(255))
    name = Column(String(255))
    code_name = Column(String(255))
    is_pal = Column(Boolean)
    tribe = Column(String(255))
    bp_class = Column(String(255))
    rarity = Column(Integer)
    element = Column(String(100))
    category = Column(String(100))
    hp = Column(Integer)
    melee_attack = Column(Integer)
    remote_attack = Column(Integer)
    defense = Column(Integer)
    support = Column(Integer)
    process_speed = Column(Float)
    capture_rate = Column(Float)
    xp_multiplier = Column(Float)
    price = Column(Integer)
    total_skills = Column(Integer)
    skill_list = Column(String(255))
    night_shift = Column(Boolean)
    partner_skill = Column(String(255))

