# combined_app.py
from pyspark.sql import SparkSession

def check_spark_version(spark_session):
    print(f"Running Spark version {spark_session.version}")

def perform_simple_operation(spark_session):
    testData = spark_session.range(100).toDF("number")
    print(f"DataFrame range(100) count: {testData.count()}")

def simple_app(spark_session, logFile):
    logData = spark_session.read.text(logFile).cache()

    numAs = logData.filter(logData.value.contains('a')).count()
    numBs = logData.filter(logData.value.contains('b')).count()

    print(f"Lines with a: {numAs}, Lines with b: {numBs}")

if __name__ == "__main__":
    # Initialize SparkSession
    spark = SparkSession.builder.appName("CombinedApp").getOrCreate()
    
    # Check Spark version and perform a simple operation to ensure it's running properly
    check_spark_version(spark)
    perform_simple_operation(spark)
    
    # Path to a text file to analyze (update with a real path on your system or environment)
    logFile = "YOUR_SPARK_HOME/README.md"
    
    # Run simple text analysis app
    simple_app(spark, logFile)
    
    # Stop the SparkSession
    spark.stop()
