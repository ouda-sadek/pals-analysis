# create_tables.py

from db.engine import get_engine
from db.base import Base
from db.models import ALL_MODELS  # pour forcer l'import des classes

def create_all_tables():
    engine = get_engine()
    print("Connexion à la base de données réussie.")

    print("Création des tables...")
    Base.metadata.create_all(bind=engine)
    print("Toutes les tables ont été créées avec succès.")

if __name__ == "__main__":
    create_all_tables()
