import pandas as pd
import sqlite3

# Load CSVs
ad_sales = pd.read_csv("ad_sales_metrics.csv")
eligibility = pd.read_csv("eligibility_table.csv")
total_sales = pd.read_csv("total_sales_metrics.csv")  # ✅ Your new file

# Save to SQLite database
conn = sqlite3.connect("ecommerce.db")
ad_sales.to_sql("ad_sales", conn, if_exists="replace", index=False)
eligibility.to_sql("eligibility", conn, if_exists="replace", index=False)
total_sales.to_sql("total_sales", conn, if_exists="replace", index=False)
conn.close()

print("✅ All tables written to ecommerce.db successfully.")
