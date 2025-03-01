This project loads financial data into a PostgreSQL database and runs ETL processes using Python.

Technologies used: Python, PostgreSQL, SQL Alchemy, Pandas, AWS RDS

Setup instructions:

1. Clone the repository:
   `git clone https://github.com/yourusername/yourrepository.git`

2. Install dependencies:
   `pip install -r requirements.txt`

3. Create a `.env` file in the root directory and add the following (replace with your actual credentials):
DATABASE_URL=postgresql://<user>:<password>@<host>:5432/<dbname>

4. Run the ETL script:
`python etl.py`
