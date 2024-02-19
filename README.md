# how it works
This project uses terraform to manage resources, github actions for CI/CD, databricks for computing, and pyspark for code.

In the pyspark file, we have a simple medallion architecture, demonstrating spoofed input data which is saved first as raw data, then cleaned and saved as the cleaned version as a silver table, then finally into a gold table which has aggregated metrics by day on device health.

For production, each stage would be saved in a real database table with surfaced dashboards available from the gold level layer and the pipeline would be unpaused.

Output from the pipeline looks like the following:
Bronze Layer:
| day        | healthy |
|------------|---------|
| 2024-01-29 | NULL    |
| 2024-02-12 | false   |
| 2024-02-16 | NULL    |
| 2024-02-05 | true    |
| 2024-02-18 | NULL    |
| 2024-02-19 | NULL    |
| 2024-02-11 | NULL    |
| 2024-02-02 | false   |
| 2024-01-21 | false   |
| 2024-02-06 | true    |
| 2024-02-01 | true    |
| 2024-02-19 | NULL    |
| 2024-02-16 | false   |
| 2024-02-16 | NULL    |
| 2024-02-17 | NULL    |
| 2024-02-12 | false   |
| 2024-01-25 | false   |
| 2024-02-01 | false   |
| 2024-02-15 | false   |
| 2024-02-10 | false   |
only showing top 20 rows

Silver Layer:
| day        | healthy |
|------------|---------|
| 2024-02-12 | false   |
| 2024-02-05 | true    |
| 2024-02-02 | false   |
| 2024-01-21 | false   |
| 2024-02-06 | true    |
| 2024-02-01 | true    |
| 2024-02-16 | false   |
| 2024-02-12 | false   |
| 2024-01-25 | false   |
| 2024-02-01 | false   |
| 2024-02-15 | false   |
| 2024-02-10 | false   |
| 2024-02-19 | true    |
| 2024-02-13 | true    |
| 2024-01-27 | true    |
| 2024-02-10 | true    |
| 2024-01-24 | true    |
| 2024-01-24 | false   |
| 2024-02-01 | true    |
| 2024-02-02 | true    |
only showing top 20 rows

Gold Layer:
| day        | percentage_healthy |
|------------|---------------------|
| 2024-01-20 | 0.57                |
| 2024-01-21 | 0.47                |
| 2024-01-22 | 0.5                 |
| 2024-01-23 | 0.68                |
| 2024-01-24 | 0.48                |
| 2024-01-25 | 0.68                |
| 2024-01-26 | 0.5                 |
| 2024-01-27 | 0.52                |
| 2024-01-28 | 0.59                |
| 2024-01-29 | 0.43                |
| 2024-01-30 | 0.36                |
| 2024-01-31 | 0.8                 |
| 2024-02-01 | 0.36                |
| 2024-02-02 | 0.56                |
| 2024-02-03 | 0.46                |
| 2024-02-04 | 0.38                |
| 2024-02-05 | 0.5                 |
| 2024-02-06 | 0.52                |
| 2024-02-07 | 0.5                 |
| 2024-02-08 | 0.33                |
only showing top 20 rows
