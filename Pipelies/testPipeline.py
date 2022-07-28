import pyspark 
from pyspark.sql import SparkSession 

server_name = "jdbc:sqlserver://PROMETHEUS\SQLEXPRESS"
database_name = "AdventureWorksDW2019"
url = server_name + ";" + "databaseName=" + database_name + ";"
table_name = "test"
username = "etl"
password = "demopass" # Please specify password here

spark = SparkSession.builder.master("local[1]") \
                    .appName("Pipelione test") \
                    .getOrCreate()

columns = ["language","users_count"]
data = [("Java", "20000"), ("Python", "100000"), ("Scala", "3000")]
df = spark.createDataFrame(data).toDF(*columns)
print(df)

# try:
#   df.write \
#     .format("com.microsoft.sqlserver.jdbc.spark") \
#     .mode("overwrite") \
#     .option("url", url) \
#     .option("dbtable", table_name) \
#     .option("user", username) \
#     .option("password", password) \
#     .save()
# except ValueError as error :
#     print("Connector write failed", error)