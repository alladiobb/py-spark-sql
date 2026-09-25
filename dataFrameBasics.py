from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("CheckNulls").getOrCreate()

data = [
    ("Alice", 28,   "Engineering", 75000),
    ("Bob",   None, "Marketing",   65000),
    ("Carol", 25,   None,          80000),
    ("Dave",  24,   "Sales",       None),
    ("Eve",   30,   "Engineering", 70000),
]
df = spark.createDataFrame(data, ["name", "age", "department", "salary"])

#CHECK FOR NULL
df.filter(col("salary").isNull()).show()

#Check not isNull
df.filter(col("salary").isNotNull()).show()

#drop null
df.dropna().show()

#drop null by column
df.filter(
    col("name").isNotNull() &
    col("age").isNotNull() &
    col("department").isNotNull() &
    col("salary").isNotNull()
).show()


df.fillna(0, subset=["salary"]).filter(col("salary").isNotNull()).show()
df.fillna(0, subset=["salary"]).show()

#Fill multiple columns with different default values
df.fillna({"age": 0, "department": "Unknown", "salary": 0}).show()

#Count how many salary values are missing
print(df.count() - df.dropna(subset=["salary"]).count())

#Count null values in the age column
print(df.filter(col("age").isNull()).count())

# DATA FRAME SHAPE 
print(df.count())

#number of columns
print(len(df.columns))

#Print the shape as a (rows, columns) tuple
print((df.count(),len(df.columns)))

print(df.count())
print(len(df.columns))

#Check whether the DataFrame is empty
print(df.count()==0)

#Print columns name
prin(df.columns)

#print a formatted shape summary
print(f"Rows: {df.count}, Columns: {len(df.columns)}")
