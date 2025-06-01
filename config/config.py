import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis un fichier .env (à la racine)
load_dotenv()

# Configuration de la base de données
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME")


# Pour debug temporaire
print("DEBUG DB_USER =", DB_USER)
# URL de connexion SQLAlchemy
DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)



