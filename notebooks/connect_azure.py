from pyspark.sql import SparkSession
from dotenv import load_dotenv
import os

spark = SparkSession.builder \
    .appName("Localspark") \
    .master("local[*]") \
    .config("spark.jars.packages",
        "com.microsoft.sqlserver:mssql-jdbc:12.6.1.jre11") \
    .getOrCreate()
spark.sparkContext.setLogLevel("ERROR")



from dotenv import load_dotenv
import os

# Load variables from .env into os.environ
load_dotenv("env")
server_name = os.environ.get("SERVERNAME")
database_name = os.environ.get("DATABASENAME")
username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")

# Standard JDBC URL format for SQL Server
jdbc_url = f"jdbc:sqlserver://{server_name}:1433;databaseName={database_name}"

#table name to read
table_name = "dbo.AP18_CUSTOMER_MASTER"

try:
    jdbcDF = spark.read \
        .format("jdbc") \
        .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver") \
        .option("url", jdbc_url) \
        .option("dbtable", table_name) \
        .option("user", username) \
        .option("password", password) \
        .load()

    # Display schema and a few rows if successful
    jdbcDF.printSchema()
    jdbcDF.show(5)

except Exception as e:
    print("JDBC read failed!")
    print("Error:", e)
