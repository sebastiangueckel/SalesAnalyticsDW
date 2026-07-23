import pandas as pd
from config.config import engine
from sqlalchemy import text

# Quelldaten einlesen
employees = pd.read_csv("../data/raw/employees.csv")

print(employees.head())
print(employees.info())
print(employees.columns)
print(employees.dtypes)

# Rohdaten einlesen
with engine.begin() as conn:
    conn.execute(text("TRUNCATE TABLE employees_raw"))

employees.to_sql(
    "employees_raw",
    engine,
    if_exists="append",
    index=False
)

print("✔ employees_raw erfolgreich befüllt.")

