import pandas as pd
from ETL.date_dim_create import date_dim
from config.config import engine
from sqlalchemy import text

customers = pd.read_csv("../data/raw/customers.csv")
products = pd.read_csv("../data/raw/products.csv")
employees = pd.read_csv("../data/raw/employees.csv")
regions = pd.read_csv("../data/raw/regions.csv")
orders = pd.read_csv("../data/raw/orders.csv")

customers["customer_key"] = range(1,len(customers)+1)
products["product_key"] = range(1,len(products)+1)
employees["employee_key"] = range(1,len(employees)+1)
regions["region_key"] = range(1,len(regions)+1)

orders = orders.merge(
    customers[["CustomerID", "customer_key"]],
    on="CustomerID",
    how="left"
)

orders = orders.merge(
    products[["ProductID", "product_key"]],
    on="ProductID",
    how="left"
)

orders = orders.merge(
    employees[["EmployeeID", "employee_key"]],
    on="EmployeeID",
    how="left"
)

customers = customers.merge(
    regions[["RegionID", "region_key"]],
    on="RegionID",
    how="left"
)

orders = orders.merge(
    customers[["CustomerID", "region_key"]],
    on="CustomerID",
    how="left"
)

orders["OrderDate"] = pd.to_datetime(orders["OrderDate"])
orders = orders.merge(
    date_dim[["date", "date_key"]],
    left_on="OrderDate",
    right_on="date",
    how="left"
)
orders = orders.drop(columns=["date"])
customers = customers.drop(columns=["region_key"])

# Einheitliche Spaltennamen
orders.columns = orders.columns.str.lower()
customers.columns = customers.columns.str.lower()
date_dim.columns = date_dim.columns.str.lower()
employees.columns = employees.columns.str.lower()
products.columns = products.columns.str.lower()
regions.columns = regions.columns.str.lower()


# Dimensionsdaten einlesen
with engine.begin() as conn:
    conn.execute(text("TRUNCATE TABLE customers_dim CASCADE"))

customers.to_sql(
    "customers_dim",
    engine,
    if_exists="append",
    index=False
)

print("✔ customers_dim erfolgreich befüllt.")

# Dimensionsdaten einlesen
with engine.begin() as conn:
    conn.execute(text("TRUNCATE TABLE date_dim CASCADE"))

date_dim.to_sql(
    "date_dim",
    engine,
    if_exists="append",
    index=False
)

print("✔ date_dim erfolgreich befüllt.")

# Dimensionsdaten einlesen
with engine.begin() as conn:
    conn.execute(text("TRUNCATE TABLE employees_dim CASCADE"))

employees.to_sql(
    "employees_dim",
    engine,
    if_exists="append",
    index=False
)

print("✔ employees_dim erfolgreich befüllt.")

# Dimensionsdaten einlesen
with engine.begin() as conn:
    conn.execute(text("TRUNCATE TABLE products_dim CASCADE"))

products.to_sql(
    "products_dim",
    engine,
    if_exists="append",
    index=False
)

print("✔ products_dim erfolgreich befüllt.")

# Dimensionsdaten einlesen
with engine.begin() as conn:
    conn.execute(text("TRUNCATE TABLE regions_dim CASCADE"))

regions.to_sql(
    "regions_dim",
    engine,
    if_exists="append",
    index=False
)

print("✔ regions_dim erfolgreich befüllt.")

# Dimensionsdaten einlesen
with engine.begin() as conn:
    conn.execute(text("TRUNCATE TABLE orders_dim CASCADE"))

orders.to_sql(
    "orders_dim",
    engine,
    if_exists="append",
    index=False
)

print("✔ orders_dim erfolgreich befüllt.")