# END TO END DATA ENGINEERING PROJECT
ADF+ SPARK + SYNAPSE + ADLS

BUSINESS REQUIREMENTS:

1. We are working for the retail clients.

2. Clients wants to have report on daily basis what is the total purchase and total revenue.

# 3.  Medallion architecture:

Medallion Architecture is a data design pattern that organizes data into distinct layers (Bronze, Silver, Gold) to improve data quality and suitability for various applications like business intelligence and machine learning. Each layer represents a stage of data refinement, with higher layers indicating better data quality.

--> source data is - REST API

# --> Bronze layer-
Fetch the data as it is from REST API to ADLS LOCATION.

# --> SILVER LAYER-
Create one dataset for the purchase, clean the data and store as parquet format.

# --> Gold layer-
Create aggregate report, what is the total purchase and reveue on daily basis and share with clients or create sql table pointing to gold dataset so client can query




