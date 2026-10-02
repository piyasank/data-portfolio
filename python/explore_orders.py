import pandas as pd
orders = pd.read_csv("data/orders.csv")
print(orders)
big_orders = orders[orders["Amount"] > 100]
print(big_orders)
totals = orders.groupby("CustomerID")["Amount"].sum()
print(totals)
exactly_80 = orders[orders["Amount"] == 80]
print(exactly_80)
customer_one = orders[orders["CustomerID"] == 3]
print(customer_one)
customers = pd.read_csv("data/customers.csv")
joined = orders.merge(customers, on= "CustomerID")
print(joined[["OrderID", "Name", "Amount"]])