from pyspark import SparkContext

# Initialize Spark Context
sc = SparkContext("local", "FruitsFilterApp")

# Define the list of fruits
fruits = [
    "apple",
    "orange",
    "apricot",
    "asparagus",
    "carrot",
    "meat"
]

# Parallelize the list to create an RDD
fruitsRDD = sc.parallelize(fruits)

# Filter words that start with the letter 'A' and count them
wordsStartingWithA = fruitsRDD.filter(lambda word: word.startswith('a'))
countWordsStartingWithA = wordsStartingWithA.count()

# Collect the filtered words and print them along with the count
filteredWords = wordsStartingWithA.collect()
print(f"Words starting with 'A': {filteredWords}")
print(f"Count of words starting with 'A': {countWordsStartingWithA}")

# Stop the Spark Context
sc.stop()
