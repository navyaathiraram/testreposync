# Databricks notebook source
# MAGIC %sh
# MAGIC nc -vz database-1-navs.cgvkkdsgxwee.ca-central-1.rds.amazonaws.com 3306

# COMMAND ----------

# MAGIC %sql 
# MAGIC show tables;

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from default.gsquarterly_march_2021_csv

# COMMAND ----------

# MAGIC %sql
# MAGIC use default

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE table1ofdb1(
# MAGIC     column1 int,
# MAGIC     column2 varchar(255),
# MAGIC     column3 int
# MAGIC   
# MAGIC );

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO table1ofdb1
# MAGIC VALUES ('1', 'DELHI', '2111');

# COMMAND ----------

import pyodbc
import os
os.environ["ODBCINI"] = "/etc/odbc.ini"
os.environ["ODBCSYSINI"] = "/etc/odbcinst.ini"
os.environ["SIMBASPARKINI"] = "/Library/simba/spark/lib/simba.sparkodbc.ini"
driver_path = "Driver=/Library/simba/spark/lib/libsparkodbc_sbu.dylib"
def get_cnxn():
    url = ";".join([
        driver_path,
        "HOST=nvn-mws2-e2.cloud.databricks.com", # replace HOST from SQL endpoint
        "PORT=443",
        "AuthMech=3",
        "UID=token",
        "SSL=1",
        "Schema=default",
        "SocketTimeout=300",
        "AutoReconnect=1",
        "ThriftTransport=2",  # binary
        "SparkServerType=3",  # thriftserver
        "HTTPPath=/sql/1.0/endpoints/06ce800a928a6782", # replace with HTTP path from SQL endpoint
        "PWD=dapi47b50c8e37325c9e7c39572923688cee",
        "RowsFetchedPerBlock=10000"
    ])
    print(url)
    cnxn = pyodbc.connect(url, autoCommit=True)
    print("Connected using ODBC..")
    return cnxn
    conn = get_cnxn()
# Set getResults to True for queries that are expected to have results (e.g., select)
# Set getResults to False for all the other queries (e.g., create table, drop table)
def run(query, getResults=False):
    print("Running query " + query)
    cursor = conn.cursor()
    cursor.execute(query)
    if getResults:
        rows = cursor.fetchall()
        for row in rows:
            print (row)
# Replace this with your code
            run("show databases", True)

# COMMAND ----------

import pyodbc
import os
os.environ["ODBCINI"] = "/etc/odbc.ini"
os.environ["ODBCSYSINI"] = "/etc/odbcinst.ini"
os.environ["SIMBASPARKINI"] = "/Library/simba/spark/lib/simba.sparkodbc.ini"
driver_path = "Driver=/Library/simba/spark/lib/libsparkodbc_sbu.dylib"
def get_cnxn():
    url = ";".join([
        driver_path,
        "HOST=nvn-mws2-e2.cloud.databricks.com", #Webapp URL
        "PORT=443",
        "AuthMech=3",
        "UID=token",
        "SSL=1",
        "Schema=default",
        "SocketTimeout=300",
        "AutoReconnect=1",
        "ThriftTransport=2",  # binary
        "SparkServerType=3",  # thriftserver
        "HTTPPath=/sql/1.0/endpoints/06ce800a928a6782", # cluster http path from cluster config
        "PWD=dapi78ea95e40f625f98dd897730cc4f16cc",
        "RowsFetchedPerBlock=10000"
    ])
    print(url)
    cnxn = pyodbc.connect(url, autoCommit=True)
    print("Connected using ODBC..")
    return cnxn
    conn = get_cnxn()
get_cnxn()

# COMMAND ----------


