import pandas as pd
from sqlalchemy import create_engine

# Connect to PostgreSQL
engine = create_engine('postgresql://postgres:Gibbygibby19@localhost/financial_warehouse')

# Sample query to get customers
query = """
SELECT * FROM customers;
"""
customers_df = pd.read_sql(query, engine)
print("Customers Data:")
print(customers_df)

# Sample query to get stocks
query = """
SELECT * FROM stocks;
"""
stocks_df = pd.read_sql(query, engine)
print("\nStocks Data:")
print(stocks_df)

# Sample query to get transactions
query = """
SELECT * FROM transactions;
"""
transactions_df = pd.read_sql(query, engine)
print("\nTransactions Data:")
print(transactions_df)
