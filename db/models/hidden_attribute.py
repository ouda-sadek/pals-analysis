# db/models/hidden_attribute.py
from sqlalchemy import Column, Integer, String, Boolean
from db.base import Base

class HiddenAttribute(Base):
    __tablename__ = "hidden_attribute"

    id = Column(Integer, primary_key=True, autoincrement=True)
    chinese_name = Column(String(255))
    code_name = Column(String(255))
    override_name_id = Column(String(255))
    prefix_id = Column(String(255))
    skill_id = Column(String(255))
    is_pal = Column(Boolean)
    tribe = Column(String(255))
    bp_class = Column(String(255))
    pictorial_id = Column(Integer)
    passive_skill_1 = Column(String(255))
    passive_skill_2 = Column(String(255))
    passive_skill_3 = Column(String(255))
    passive_skill_4 = Column(String(255))
