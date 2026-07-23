import pandas as pd
from config.config import engine
from sqlalchemy import text

# Quelldaten einlesen
regions = pd.read_csv("../data/raw/regions.csv")

print(regions.head())
print(regions.info())
print(regions.columns)
print(regions.dtypes)

# Rohdaten einlesen
with engine.begin() as conn:
    conn.execute(text("TRUNCATE TABLE regions_raw"))

regions.to_sql(
    "regions_raw",
    engine,
    if_exists="append",
    index=False
)

print("✔ regions_raw erfolgreich befüllt.")