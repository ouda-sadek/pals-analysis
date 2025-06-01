import os
import pandas as pd
from sqlalchemy import create_engine

# Connect to your MariaDB database (adjust user/password if necessary)
engine = create_engine("mariadb+mariadbconnector://root:Nassima_13@localhost:3306/palworld_database")

# Path to the "data" directory (at the same level as "database")
base_dir = os.path.dirname(os.path.dirname(__file__))  # go up to "pals-analysis"
csv_dir = os.path.join(base_dir, "data")

# Mapping of file names to corresponding table names
file_to_table = {
    "Palworld_Data--Palu combat attribute table.csv": "combat_attribute",
    "Palworld_Data-Palu Job Skills Table.csv": "job_skill",
    "Palworld_Data-hide pallu attributes.csv": "hidden_attribute",
    "Palworld_Data--Palu refresh level.csv": "refresh_area",
    "Palworld_Data-comparison of ordinary BOSS attributes.csv": "ordinary_boss_attribute",
    "Palworld_Data-Tower BOSS attribute comparison.csv": "tower_boss_attribute",
}

# Loop through each file and import it into the corresponding table
for filename, table_name in file_to_table.items():
    file_path = os.path.join(csv_dir, filename)
    if os.path.exists(file_path):
        print(f"Importing {filename} into table '{table_name}'")

        df = pd.read_csv(file_path)

        # Clean column names
        df.columns = (
            df.columns
            .str.strip()  # remove leading/trailing spaces
            .str.lower()  # lowercase
            .str.replace(' ', '_')  # replace spaces with underscores
            .str.replace('[^0-9a-zA-Z_]', '', regex=True)  # remove special characters
            .str[:60]  # limit column name length
        )

        # Import into MariaDB
        df.to_sql(name=table_name, con=engine, if_exists="replace", index=False)

        print(f"Done: {table_name}")
    else:
        print(f"File not found: {file_path}")
