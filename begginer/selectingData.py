from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Select").getOrCreate()

data = [
    ("Alice", 28, "Engineering", 75000),
    ("Bob",   32, "Marketing",   65000),
    ("Carol", 25, "Engineering", 80000),
    ("Dave",  24, "Sales",       60000),
]
df = spark.createDataFrame(data, ["name", "age", "department", "salary"])


#Select a single column
df.select("name").show()

#Select two specific columns
df.select("name","salary").show()

df.select("name", "age", "department").show()

#reorder columns with select
df.select("salary", "name").orderBy().show()

cols = ["name", "department"]
df.select(cols).show()

#Select columns and verify the result shape
selected = df.select("name","age")
print(selected.count())
print(len(selected.columns))

#COLUMN ALIAS
df.select("name",df["salary"].alias("annual_salary")).show()

df.select(
    df["name"].alias("emp_name"),
    df["department"].alias("team"),
    df["salary"].alias("salary_usd"),
).show()

df.select("name", col("salary").alias("salary_usd")).show()

df.select(
    col("name").alias("full_name"),
    col("age").alias("age_years"),
    col("department").alias("team"),
    col("salary").alias("annual_pay"),
).show()

df.select(
    "name",
    "salary",
    (col("salary") * 2).alias("double_salary"),
).show()

renamed = df.select(
    col("name").alias("employee_name"),
    col("salary").alias("annual_salary"),
)
renamed.show()

#reorder

df.select(
    df["salary"].alias("annual_salary"),
    "name",
).show()

df.select(col("name"), col("salary")).show()

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("RenameAll").getOrCreate()

data = [
    ("Alice", 28, "Engineering", 75000),
    ("Bob",   32, "Marketing",   65000),
    ("Carol", 25, "Engineering", 80000),
    ("Dave",  24, "Sales",       60000),
]
df = spark.createDataFrame(data, ["name", "age", "department", "salary"])
df.select(
    col("name").alias("full_name"),
    col("age").alias("age_years"),
    col("department").alias("team"),
    col("salary").alias("annual_pay"),
).show()

#Build a dynamic column list and use it with col() in select()

df = spark.createDataFrame(data, ["name", "age", "department", "salary"])

cols_to_select = ["name", "department"]

df.select([col(c) for c in cols_to_select]).show()


#drop
df.drop("age").show()
df.drop("age", "salary").show()

cols_to_drop = ["age", "department"]
df.drop(*cols_to_drop).show()

# SELECT DISTINCT VALUES
df.select("department").distinct().show()

#sorted alphabetically descending
df.select("department").distinct().orderBy("department", ascending=False).show()

#drop duplicates
df.dropDuplicates(["department"]).show()

#distintc on the full date table
df.distinct().show()

##COMPUTED COLUMN SELECT
df.withColumn("annual_salary", df["salary"] * 12).select("name", "annual_salary").show()

#CATEGOSIRE SALARY UNTO BANDS USING WHEN / otherwise
df.withColumn("salary_band", when(df["salary"] < 65000, "Low")
    .when(df["salary"] >= 80000, "High")
    .otherwise("Mid"))
    .select("name", "salary", "salary_band")
    .show()

#calcule percentagem
df.withColumn("bonus", df["salary"] * 0.1).select("name", "salary", "bonus").show()

#build a display label with concat, upper and lit 
df.withColumn("full_label", concat(upper(col("name")), lit(" - "), col("department")))
    .select("full_label").show()

#cast a column
df.withColumn("salary_str", df["salary"].cast("string"))
    .select("name", "salary_str").show()

#add an experience level label based on age
df.withColumn("experience_level", when(df["age"] < 25, "Junior")
.when(df["age"] > 30, "Senior").otherwise("Mid")).show()

#Add multiple computed columns in sequence
df.withColumn("annual_salary", df["salary"] * 12)
    .withColumn("tax", df["salary"] * 0.3)
    .select("name", "salary", "annual_salary", "tax")
    .show()

#uppercase
df.withColumn("dept_upper", upper(col("department"))).select("name", "dept_upper").show()

