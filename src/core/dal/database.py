import psycopg2

from src.config import config

# connect() is function in package psycopg2
# it creates new database connection

db_details = config['db_details']

connection = psycopg2.connect(
    host=db_details['host'],
    database=db_details['database'],
    user=db_details['user'],
    port=db_details['port'],
    password=db_details['password']
)
