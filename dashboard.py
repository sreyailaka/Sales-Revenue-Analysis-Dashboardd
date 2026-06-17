import pandas as pd

df = pd.read_csv("sales_data.csv")

total_revenue = df["Revenue"].sum()
total_quantity = df["Quantity"].sum()

print("Sales & Revenue Analysis Dashboard")
print("----------------------------------")
print("Total Revenue:", total_revenue)
print("Total Products Sold:", total_quantity)

top_product = df.loc[df["Revenue"].idxmax(), "Product"]
print("Top Performing Product:", top_product)