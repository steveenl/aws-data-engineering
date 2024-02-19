from pyspark.sql import SparkSession
from datetime import datetime, timedelta
import random

spark = SparkSession.builder.appName("DeviceHealthMedallionArchitecture").getOrCreate()

def random_health_status():
    return random.choice([True, False]) if random.random() < 0.9 else None

def random_date():
    days_ago = random.randint(0, 30)
    return datetime.now().date() - timedelta(days=days_ago)

# Generate dirty dummy data with occasional missing values (BRONZE Layer)
data = [(random_date(), random_health_status()) for _ in range(1000)]
df = spark.createDataFrame(data, ["day", "healthy"])
df.createOrReplaceTempView("bronze")
print("Bronze Layer:")
spark.sql("SELECT * FROM bronze").show()

# Clean the data by filtering out records with missing values (SILVER Layer)
silver_df = spark.sql("SELECT * FROM bronze WHERE healthy IS NOT NULL")
silver_df.createOrReplaceTempView("silver")
print("Silver Layer:")
spark.sql("SELECT * FROM silver").show()

# Aggregate data to find the percentage of healthy devices per day (GOLD Layer)
aggregated_df = spark.sql("""
    SELECT day, 
           ROUND(AVG(CAST(healthy AS INT)), 2) AS percentage_healthy 
    FROM silver 
    GROUP BY day
    ORDER BY day
""")
aggregated_df.createOrReplaceTempView("gold")
print("Gold Layer:")
spark.sql("SELECT * FROM gold").show()
