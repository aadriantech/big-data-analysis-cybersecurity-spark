from pyspark import SparkContext

# Initialize Spark Context
sc = SparkContext("local", "PySparkBasics")

def perform_simple_operation():
    nums = list(range(0, 1000001))
    nums_rdd = sc.parallelize(nums)
    #print(nums_rdd.collect())
    #print(nums_rdd.take(5))
    squared_nums_rdd = nums_rdd.map(lambda x: x ** 2)
    #print(squared_nums_rdd.take(5))
    pairs = squared_nums_rdd.map(lambda x: (x, len(str(x))))
    #print(pairs.take(25))
    even_digit_pairs = pairs.filter(lambda x: (x[1] % 2) == 0)
    #print(even_digit_pairs.take(25))
    flipped_pairs = even_digit_pairs.map(lambda x: (x[1], x[0]))
    flipped_pairs.take(25)
    grouped = flipped_pairs.groupByKey()
    grouped = grouped.map(lambda x: (x[0], list(x[1])))
    grouped.take(2)
    averaged = grouped.map(lambda x: (x[0], sum(x[1]) / len(x[1])))
    print(averaged.collect())

if __name__ == "__main__":
    perform_simple_operation()
    sc.stop()
