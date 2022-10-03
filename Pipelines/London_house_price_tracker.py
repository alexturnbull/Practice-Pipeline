import pandas as pd 
import requests 
import pypyodbc as odbc
import os 
from datetime import date 
from sqlalchemy.engine import URL
from sqlalchemy import create_engine

downloadUrl = 'https://www.ons.gov.uk/generator?uri=/economy/inflationandpriceindices/bulletins/housepriceindex/february2022/61b62a24&format=csv'

# Scrape CSV from ONS website 

today = date.today()

with requests.get(downloadUrl) as rq:
      with open(f"C:\\Data\\ONS\\housing_prices\\housing_prices_{today}.csv", 'wb') as file:
          file.write(rq.content)
    

# Read CSV in as dataframe
RawData = pd.read_csv("C:\\Data\\ONS\\housing_prices\\housing_prices_2022-08-30.csv", header=6)

#Drop all but london 
LondonData = RawData.drop(['North East', 'North West', 'Yorkshire and The Humber', 'East Midlands', 'West Midlands', 'East', 'South East', 'South West'], axis=1)
print(LondonData)



#write to sql 
DRIVER_NAME = '{SQL Server}'
SERVER_NAME = 'PROMETHEUS\SQLEXPRESS'
DATABASE_NAME ='AdventureWorksDW2019'
PASS = os.environ.get('PASSOS')
USER = os.environ.get('USEROS')

connection_string_admin = f"""DRIVER={DRIVER_NAME}; SERVER={SERVER_NAME}; DATABASE={DATABASE_NAME}; Trust_Connection=yes"""
#connection_string_etl = f"""DRIVER={DRIVER_NAME}; SERVER={SERVER_NAME}; DATABASE={DATABASE_NAME}; UID={USER}; PWD={PASS}"""

connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string_admin})
engine = create_engine(connection_url) 

LondonData.to_sql(name='London_house_price', con=engine, schema='dbo', if_exists='replace', index=False)