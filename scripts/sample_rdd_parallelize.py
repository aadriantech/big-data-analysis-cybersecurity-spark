from pyspark.sql import SparkSession

def perform_simple_operation(spark_session):
    # Using RDD to perform a simple operation: creating a range of numbers and counting them
    numbersRDD = spark_session.sparkContext.parallelize(range(100))
    print(f"Range(100) RDD count: {numbersRDD.count()}")

def simple_app_rdd(spark_session):
    # Define a list of strings to analyze
    logLines = [
        "This is an example log line with a",
        "Another log line without the letter",
        "This log line has both a and b",
        "Neither a nor b is present here",
        "Here is another line with a, and here's a b as well"
    ]
    
    # Create an RDD from the list of strings
    logLinesRDD = spark_session.sparkContext.parallelize(logLines)
    
    # Filter lines containing 'a' and 'b', then count them
    numAs = logLinesRDD.filter(lambda line: 'a' in line).count()
    numBs = logLinesRDD.filter(lambda line: 'b' in line).count()
    
    print(f"Lines with 'a': {numAs}, Lines with 'b': {numBs}")

if __name__ == "__main__":
    # Initialize SparkSession
    spark = SparkSession.builder.appName("SimpleRDDApp").getOrCreate()
    
    # Perform a simple operation to demonstrate RDD functionality
    perform_simple_operation(spark)
    
    # Run the application that analyzes the hardcoded list of strings using RDDs
    simple_app_rdd(spark)
    
    # Stop the SparkSession
    spark.stop()
