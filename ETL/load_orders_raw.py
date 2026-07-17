import pandas as pd
from config.config import engine
from sqlalchemy import text

# Quelldaten einlesen
orders = pd.read_csv("../data/raw/orders.csv")

# Einheitliche Spaltennamen
orders.columns = orders.columns.str.lower()

# Rohdaten einlesen
with engine.begin() as conn:
    conn.execute(text("TRUNCATE TABLE orders_raw"))

orders.to_sql(
    "orders_raw",
    engine,
    if_exists="append",
    index=False
)

print("✔ orders_raw erfolgreich befüllt.")