from pyspark.sql import SparkSession
import pandas as pd

spark = SparkSession.builder.appName("Datacamp Pyspark Tutorial").config("spark.memory.offHeap.enabled","true").config("spark.memory.offHeap.size","10g").getOrCreate()

# Load data from specified path "csv file"
data_path = "/app/data/online_retail.csv"
df = spark.read.csv(data_path,header=True,escape="\"")
result = df.show(5,0)
print(result)