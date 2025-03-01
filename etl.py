import pandas as pd
from sqlalchemy import create_engine

# Connect to PostgreSQL
engine = create_engine('postgresql://postgres:Gibbygibby19@localhost/financial_warehouse')

# Sample data
customers = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'email': ['alice@example.com', 'bob@example.com', 'charlie@example.com'],
    'country': ['USA', 'UK', 'Germany']
})

stocks = pd.DataFrame({
    'symbol': ['AAPL', 'GOOGL', 'AMZN'],
    'company_name': ['Apple', 'Google', 'Amazon'],
    'sector': ['Technology', 'Technology', 'E-commerce']
})

transactions = pd.DataFrame({
    'customer_id': [1, 2, 1],
    'stock_id': [1, 2, 3],
    'date_id': [1, 1, 2],
    'transaction_type': ['BUY', 'SELL', 'BUY'],
    'quantity': [10, 5, 20],
    'price': [150.5, 2800.1, 3400.0]
})

# Load data into database
customers.to_sql('customers', engine, if_exists='append', index=False)
stocks.to_sql('stocks', engine, if_exists='append', index=False)
transactions.to_sql('transactions', engine, if_exists='append', index=False)

print("Data loaded successfully!")
