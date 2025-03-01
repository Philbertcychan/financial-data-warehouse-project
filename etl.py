from sqlalchemy import create_engine
import os
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the database URL from the environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

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

# Test database connection
try:
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()
    print("Connection successful!")

    # Load data into the database
    customers.to_sql('customers', engine, if_exists='replace', index=False)
    stocks.to_sql('stocks', engine, if_exists='replace', index=False)
    transactions.to_sql('transactions', engine, if_exists='replace', index=False)

    print("Data loaded successfully!")

    connection.close()
except Exception as e:
    print(f"Error: {e}")
