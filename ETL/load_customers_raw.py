import pandas as pd
from config.config import engine
from sqlalchemy import text

# Quelldaten einlesen
customers = pd.read_csv("../data/raw/customers.csv")
print(customers.head())
print(customers.info())
print(customers.columns)

# Einheitliche Spaltennamen
customers.columns = customers.columns.str.lower()

# Rohdaten einlesen
with engine.begin() as conn:
    conn.execute(text("TRUNCATE TABLE orders_raw"))

customers.to_sql(
    "customers_raw",
    engine,
    if_exists="append",
    index=False
)

print("✔ customers_raw erfolgreich befüllt.")