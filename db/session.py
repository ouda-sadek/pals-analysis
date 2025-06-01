# db/session.py

from sqlalchemy.orm import sessionmaker
from db.engine import get_engine

# Obtenir l'engine configuré (via config/config.py)
engine = get_engine()

# Créer une fabrique de session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
