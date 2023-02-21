# Databricks notebook source
import requests
wid = input("Enter workspace URL: ")
data = requests.get(wid)
print (data)

dbutils.fs.ls("dbfs:/FileStore")
