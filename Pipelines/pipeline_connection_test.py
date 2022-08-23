import pypyodbc as odbc
import os 
import pandas as pd
from sqlalchemy.engine import URL
from sqlalchemy import create_engine

DRIVER_NAME = '{SQL Server}'
SERVER_NAME = 'PROMETHEUS\SQLEXPRESS'
DATABASE_NAME ='AdventureWorksDW2019'
PASS = os.environ.get('PASSOS')
USER = os.environ.get('USEROS')

connection_string_admin = f"""DRIVER={DRIVER_NAME}; SERVER={SERVER_NAME}; DATABASE={DATABASE_NAME}; Trust_Connection=yes"""
#connection_string_etl = f"""DRIVER={DRIVER_NAME}; SERVER={SERVER_NAME}; DATABASE={DATABASE_NAME}; UID={USER}; PWD={PASS}"""

connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string_admin})
engine = create_engine(connection_url) 
df = pd.read_sql_query("SELECT TOP 100 * FROM dbo.DimAccount WHERE AccountDescription = 'Assets'", engine)
df.to_sql(name='Asset_Accounts', con=engine, schema='dbo', if_exists='replace', index=False)