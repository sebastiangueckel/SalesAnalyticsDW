import pandas as pd
from config.config import engine
from sqlalchemy import text

# Quelldaten einlesen
products = pd.read_csv("../data/raw/products.csv")

print(products.head())
print(products.info())
print(products.columns)
print(products.dtypes)

# Rohdaten einlesen
with engine.begin() as conn:
    conn.execute(text("TRUNCATE TABLE products_raw"))

products.to_sql(
    "products_raw",
    engine,
    if_exists="append",
    index=False
)

print("✔ products_raw erfolgreich befüllt.")