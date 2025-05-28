import pandas as pd
from sqlalchemy import create_engine

# Configuration of the MariaDB database
USER = "root"
PASSWORD = "Nassima_13"
HOST = "localhost"
PORT = "3306"
DB_NAME = "palworld_database"

# Connection to the base
engine = create_engine(f"mariadb+mariadbconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}")

# Upload CSV file
csv_path = "./data/Palworld_Data--Palu combat attribute table.csv"
df = pd.read_csv(csv_path)

# Show columns for validation
print("Colonnes du fichier CSV :", df.columns.tolist())

# Cleaning/renaming (to be adapted according to the exact names of the columns)
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Import into MariaDB
df.to_sql(name="combat_attribute", con=engine, if_exists="replace", index=False)

print("Table 'combat_attribute' successfully imported !")
