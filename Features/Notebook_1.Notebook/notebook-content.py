# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "db7c3ad9-c636-4c60-a270-25afcea2a6e4",
# META       "default_lakehouse_name": "myLake1",
# META       "default_lakehouse_workspace_id": "ff136b77-1d11-4a10-bbcc-6221cc2bd160",
# META       "known_lakehouses": [
# META         {
# META           "id": "db7c3ad9-c636-4c60-a270-25afcea2a6e4"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

print("hi")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%configure
# MAGIC {
# MAGIC   "defaultLakehouse": {
# MAGIC     "name": "myLake1"
# MAGIC   }
# MAGIC }
# MAGIC 


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC CREATE TABLE products
# MAGIC USING DELTA
# MAGIC LOCATION 'Files/external_products';

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC 
# MAGIC CREATE EXTERNAL TABLE ProductsJson (
# MAGIC     id INT,
# MAGIC     name STRING,
# MAGIC     category STRING,
# MAGIC     price INT,
# MAGIC     inStock BOOLEAN,
# MAGIC     rating DECIMAL(3,1)
# MAGIC )
# MAGIC USING JSON
# MAGIC LOCATION 'Files/products/';
# MAGIC 
# MAGIC 
# MAGIC 


# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.sql("SELECT * FROM myLake1.productsjson LIMIT 1000")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
