#FILTER ROWS
df.filter(df["age"] > 25).show()
df.filter(df["department"] != "Sales").show()

#using cols
df.filter(col("salary") > 70000).show()

print(f"Filtered count: {df.filter(df['age'] > 25).count()}")

#using WHERE
df.where(df["department"] == "Engineering").show()
df.where(df["age"] >= 30).show()

#using COL
df.where(col("salary") > 70000).show()


df.where(df["department"] == "Engineering")
    .where(df["salary"] > 70000).show()

df.where((df["department"] == "Engineering") | (df["department"] == "Sales")).show()

df.withColumn("bonus", col("salary") * 0.1).where(col("bonus") > 7000).show()

filter_count = df.filter(df["salary"] >= 75000).count()
where_count = df.where(df["salary"] >= 75000).count()
print(f"filter: {filter_count}, where: {where_count}")

df.filter((df["department"] == "Engineering") & (df["salary"] >= 75000)).show()

df.filter((df["department"] == "Engineering") | (df["department"] == "Sales")).show()

#NOT - exclude rows with ~(tilde)
df.filter(~(df["department"] == "Marketing")).show()

df.filter((df["department"] == "Engineering") 
    & (df["age"] < 30) 
    & (df["salary"] >= 75000)).show()

df.filter(((df["department"] == "Engineering") 
    | (df["department"] == "Sales")) 
    & (df["salary"] > 62000)).show()

df.filter(~col("department")
    .isin("Marketing", "Sales"))
    .show()

#ISIN
df.filter(df["department"]
    .isin("Engineering", "Sales"))
    .show()

allowed = ["Engineering", "Sales"]
df.filter(df["department"]
    .isin(*allowed))
    .show()

df.filter(~col("department")
    .isin("Marketing", "Sales"))
    .show()

df.filter(col("department")
    .isin("Engineering", "Marketing")
    & (col("salary") >= 70000))
    .show()

result = df.filter(df["department"]
    .isin("Engineering", "Sales"))
    .count()
print(f"Matching rows: {result}")

#null values
df.filter(col("salary").isNull()).show()
df.filter(col("salary").isNotNull()).show()
df.filter(col("age").isNull() | col("department").isNull() | col("salary").isNull()).show()

df.dropna(subset=["salary"]).show()

#filter rows where a column contains a substring
df.filter(col("department").contains("ing")).show()

#start with
df.filter(col("department").startswith("Eng")).show()

#end with
df.filter(col("name").endswith("e")).show()

#Exclude rows using NOT contains with ~
df.filter(~col("department").contains("ing")).show()

df.filter(col("department").contains("ing") & (col("salary") > 70000)).show()

df.filter(col("department").startswith("Eng") | col("name").endswith("b")).show()

df.filter(lower(col("department")).contains("engineering")).show()

#between
df.filter(col("salary").between(65000, 80000)).show()

#Filter rows outside a salary range using ~between()
df.filter(~col("salary").between(65000, 80000)).show()

df.filter(col("salary").between(65000, 80000) & col("department").contains("ing")).show()

df.filter(col("salary").between(65000, 80000)).orderBy(col("salary").desc()).show()

df.filter(col("age").between(24, 28)).select("name", "salary").show()

df.filter((col("salary") >= 65000) & (col("salary") <= 80000)).show()

df.filter(col("age").between(24, 30) & col("salary").between(70000, 85000)).show()

#Exclude rows where name starts with a prefix
df.filter(~col("name").startswith("A")).show()

