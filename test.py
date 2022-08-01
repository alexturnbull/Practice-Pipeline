import pypyodbc as odbc
import os 

DRIVER_NAME = '{SQL Server Native Client 11.0}'
SERVER_NAME = 'PROMETHEUS\SQLEXPRESS'
DATABASE_NAME ='AdventureWorksDW2019'
#pwd = os.environ.get('PASSOS')
#uid = os.environ.get('USEROS')


connection_string = f"""DRIVER={DRIVER_NAME}; SERVER= {SERVER_NAME}; DATABASE={DATABASE_NAME}; Trust_Connection=yes'"""


conn = odbc.connect(connection_string)
print(conn)