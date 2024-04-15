import pandas as pd
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import seaborn as sns
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import StandardScaler
from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator

spark = SparkSession.builder.appName("Datacamp Pyspark Tutorial") \
    .config("spark.memory.offHeap.enabled","true") \
    .config("spark.memory.offHeap.size","10g") \
    .getOrCreate()

# Load data from specified path "xlsx file"
data_path = "/app/data/online_retail.xlsx"

# Read the Excel file using pandas
pd_df = pd.read_excel(data_path)

# Create a Spark DataFrame from the pandas DataFrame
df = spark.createDataFrame(pd_df) 

#result = df.show(5,0)
# print(result)
# print(f"number of rows in the dataframe {df.count()}") # Answer: 541,909
#df.select('CustomerID').distinct().count()
#df.groupBy('Country').agg(countDistinct('CustomerID').alias('country_count')).orderBy(desc('country_count')).show()

#spark.sql("set spark.sql.legacy.timeParserPolicy=LEGACY")
#df = df.withColumn('date',to_timestamp("InvoiceDate", 'yy/MM/dd HH:mm'))
#df.select(max('date')).show()
#df.select(min("date")).show()

# Recency Data
#df = df.withColumn("from_date", lit("12/1/10 08:26"))
#df = df.withColumn('from_date',to_timestamp("from_date", 'yy/MM/dd HH:mm'))
#df2 = df.withColumn('from_date',to_timestamp(col('from_date'))).withColumn('recency',col("date").cast("long") - col('from_date').cast("long"))
#df2 = df2.join(df2.groupBy('CustomerID').agg(max('recency').alias('recency')),on='recency',how='leftsemi')
#df2.show(5,0)
#df2.printSchema()

# Recency Data V2
# Calculate the minimum date in the dataset
min_date = df.select(min('InvoiceDate')).collect()[0][0]

# Set the from_date as the minimum date
df = df.withColumn("from_date", lit(min_date))

# Convert columns to timestamp format
df = df.withColumn('date', to_timestamp("InvoiceDate", 'yy/MM/dd HH:mm'))
df = df.withColumn('from_date', to_timestamp("from_date", 'yy/MM/dd HH:mm'))

# Calculate recency
df = df.withColumn('recency', col("date").cast("long") - col('from_date').cast("long"))

# Join with maximum recency per CustomerID
df2 = df.join(df.groupBy('CustomerID').agg(max('recency').alias('recency')), on='recency', how='leftsemi')

# Show the first 5 rows and schema
df2.show(5, False)
df2.printSchema()
# end recency v2

# Frequency Column
df_freq = df2.groupBy('CustomerID').agg(count('InvoiceDate').alias('frequency'))
df_freq.show(5,0)
df3 = df2.join(df_freq,on='CustomerID',how='inner')
df3.printSchema()

m_val = df3.withColumn('TotalAmount',col("Quantity") * col("UnitPrice"))
m_val = m_val.groupBy('CustomerID').agg(sum('TotalAmount').alias('monetary_value'))
finaldf = m_val.join(df3,on='CustomerID',how='inner')
finaldf = finaldf.select(['recency','frequency','monetary_value','CustomerID']).distinct()
finaldf.show(5,0)

assemble=VectorAssembler(inputCols=[
    'recency','frequency','monetary_value'
], outputCol='features')

assembled_data=assemble.transform(finaldf)

scale=StandardScaler(inputCol='features',outputCol='standardized')
data_scale=scale.fit(assembled_data)
data_scale_output=data_scale.transform(assembled_data)
data_scale_output.select('standardized').show(2,truncate=False)

# Let’s run the following lines of code to build a K-Means clustering algorithm from 2 to 10 clusters:
cost = np.zeros(10)

evaluator = ClusteringEvaluator(predictionCol='prediction', featuresCol='standardized',metricName='silhouette', distanceMeasure='squaredEuclidean')

for i in range(2,10):
    KMeans_algo=KMeans(featuresCol='standardized', k=i)
    KMeans_fit=KMeans_algo.fit(data_scale_output)
    output=KMeans_fit.transform(data_scale_output)
    cost[i] = KMeans_fit.summary.trainingCost
    

df_cost = pd.DataFrame(cost[2:])
df_cost.columns = ["cost"]
new_col = range(2,10)
df_cost.insert(0, 'cluster', new_col)

# pl.plot(df_cost.cluster, df_cost.cost)
# pl.xlabel('Number of Clusters')
# pl.ylabel('Score')
# pl.title('Elbow Curve')
# pl.show()

# Save the graph image
plt.plot(df_cost.cluster, df_cost.cost)
plt.xlabel('Number of Clusters')
plt.ylabel('Score')
plt.title('Elbow Curve')
plt.savefig('/app/data/elbow_curve_machine_learning.png')

KMeans_algo=KMeans(featuresCol='standardized', k=4)
KMeans_fit=KMeans_algo.fit(data_scale_output)
preds=KMeans_fit.transform(data_scale_output)
preds.show(5,0)

# Cluster Analysis
df_viz = preds.select('recency','frequency','monetary_value','prediction')
df_viz = df_viz.toPandas()
avg_df = df_viz.groupby(['prediction'], as_index=False).mean()

list1 = ['recency','frequency','monetary_value']

# for i in list1:
#     sns.barplot(x='prediction',y=str(i),data=avg_df)
#     #plt.show()
#     plt.savefig('/app/data/elbow_curve_machine_learning.png')

# Define a function to create and save bar plots for each feature
def create_and_save_barplot(feature, avg_df):
  plt.figure(figsize=(8, 6))  # Set desired figure size
  sns.barplot(x='prediction', y=feature, data=avg_df)
  plt.xlabel('Prediction')
  plt.ylabel(feature)
  plt.title(f'{feature} by Prediction')
  filename = f'{feature}_by_prediction.png'  # Customize filenames
  plt.savefig(f'/app/data/{filename}', dpi=300)  # Save with high-quality resolution
  plt.close()  # Close the figure to avoid memory issues

# Create and save bar plots for each feature
for feature in list1:
  create_and_save_barplot(feature, avg_df)
