from sqlalchemy import create_engine
import pyodbc
import pandas as pd
import os

#get password from environmnet var
pwd = os.environ.get('PASSOS')
uid = os.environ.get('USEROS')
#sql db details
driver = "{SQL Server Native Client 11.0}"
server = "PROMETHEUS"
database = "AdventureWorksDW2019;"

#extract data from sql server
def extract(driver, server, database, uid, pwd):
    try:
        src_conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + '\SQLEXPRESS' + ';DATABASE=' + database + ';UID=' + uid + ';PWD=' + pwd)
        # src_cursor = src_conn.cursor()
        # # execute query
        # src_cursor.execute(""" SELECT  EnglishDayNameOfWeek
        # from dbo.DimDate """)
        #query and load save data to dataframe
        df = pd.read_sql_query(f'select * FROM EnglishDayNameOfWeek', src_conn)
        load(df, 'EnglishDayNameOfWeek')
    except Exception as e:
        print("Data extract error: " + str(e))
    finally:
        src_conn.close()


df = extract(driver, server, database, uid, pwd)

# #load data to postgres
# def load(df, tbl):
#     try:
#         rows_imported = 0
#         engine = create_engine(f'postgresql://{uid}:{pwd}@{server}:5432/AdventureWorks')
#         print(f'importing rows {rows_imported} to {rows_imported + len(df)}... for table {tbl}')
#         # save df to postgres
#         df.to_sql(f'stg_{tbl}', engine, if_exists='replace', index=False)
#         rows_imported += len(df)
#         # add elapsed time to final print out
#         print("Data imported successful")
#     except Exception as e:
#         print("Data load error: " + str(e))

# try:
#     #call extract function
#     extract()
# except Exception as e:
#     print("Error while extracting data: " + str(e))