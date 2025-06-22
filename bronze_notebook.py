# Bronze Layer - Ingest JSON from ADLS
from pyspark.sql.functions import col, to_date, lower
df_bronze = spark.read.parquet("abfss://datafiles@vaishnaviadlsgen2june.dfs.core.windows.net/bronze/VAISHNAVI7382/azure-datafactory-project1/refs/heads/main/retail_transactions_bronze.parquet")
df_bronze.show()
