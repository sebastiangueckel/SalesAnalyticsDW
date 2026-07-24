import pandas as pd
from ETL.date_dim_create import date_dim

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

print(orders.columns)