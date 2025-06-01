# db/models/__init__.py

from .combat_attribute import CombatAttribute
from .job_skill import JobSkill
from .hidden_attribute import HiddenAttribute
from .refresh_area import RefreshArea
from .ordinary_boss_attribute import OrdinaryBossAttribute
from .tower_boss_attribute import TowerBossAttribute

# Optionnel : liste pour import dynamique
ALL_MODELS = [
    CombatAttribute,
    JobSkill,
    HiddenAttribute,
    RefreshArea,
    OrdinaryBossAttribute,
    TowerBossAttribute,
]
