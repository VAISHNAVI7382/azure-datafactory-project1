# Bronze Layer - Ingest JSON from ADLS
from pyspark.sql.functions import col, to_date, lower
df_bronze = spark.read.parquet("https://vaishnaviadlsgen2june.blob.core.windows.net/datafiles/bronze/VAISHNAVI7382/azure-datafactory-project1/refs/heads/main/retail_transactions_bronze.parquet")
df_bronze.show()
