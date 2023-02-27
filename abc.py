# Databricks notebook source
import requests
wid = input("Enter workspace URL: ")
data = requests.get(wid)
print (data)

# COMMAND ----------

# MAGIC %sh traceroute adb-624783076386327.7.azuredatabricks.net

# COMMAND ----------

# MAGIC %sql select current_metastore()

# COMMAND ----------

dbutils.fs.ls("dbfs:/FileStore")
