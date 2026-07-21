# Exercise 25 – Incremental Data Loading

## Overview

This exercise demonstrates the implementation of an **incremental data loading process** using PostgreSQL. Incremental loading is a key concept in ETL (Extract, Transform, Load) pipelines where only new or changed records are loaded into a database instead of processing the entire dataset repeatedly.

In real-world data engineering environments, data is continuously generated from different sources. Reloading millions of existing records every day is inefficient, consumes unnecessary resources, and increases processing time. Incremental loading solves this problem by identifying and inserting only new records while avoiding duplicates.

In this exercise, two daily CSV files were created:

* `sensor_data_day1.csv` – Represents the initial dataset.
* `sensor_data_day2.csv` – Represents new incoming data containing both existing and new records.

The objective was to load Day 1 data first, then process Day 2 data and insert only records that did not already exist in the database.

---

# Exercise Objectives

The objectives of this exercise were to:

1. Understand the concept of incremental loading in ETL pipelines.
2. Create daily CSV datasets representing incoming data.
3. Perform an initial database load from Day 1 data.
4. Create a staging table for incoming Day 2 data.
5. Compare incoming records against existing database records.
6. Prevent duplicate records from being inserted.
7. Load only new records into the production table.
8. Verify the final database state.

---

# Technologies Used

* Linux Command Line
* PostgreSQL 13
* SQL
* CSV Files
* ETL Concepts

---

# Key Definitions

## Incremental Load

Incremental loading is a data processing method where only new or modified records are added to a database instead of replacing the entire dataset.

Example:

A company receives 1 million new transactions every day. Instead of reloading the entire transaction database, the ETL pipeline only loads the 1 million new transactions.

---

## Staging Table

A staging table is a temporary storage area used during ETL processing.

Incoming data is first loaded into the staging table where it can be:

* validated,
* cleaned,
* checked for duplicates,
* transformed before entering the main database table.

---

## Duplicate Record

A duplicate record is a record that already exists in the target database.

In this exercise, the `id` column was used as the unique identifier to determine whether a record already existed.

---

# ETL Workflow

The process followed this architecture:

```
sensor_data_day1.csv
          |
          |
          v
Initial Database Load
          |
          |
          v
sensor_readings Table


sensor_data_day2.csv
          |
          |
          v
Temporary Staging Table
          |
          |
          v
Duplicate Check
          |
          |
          v
Insert New Records Only
          |
          |
          v
Updated sensor_readings Table
```

---

# Step 1 – Reset Database Table

The existing table was cleared before beginning the exercise:

```sql
TRUNCATE TABLE sensor_readings;
```

## Purpose

This command removed all existing records while keeping the table structure.

It allowed the exercise to simulate a fresh production environment.

---

# Step 2 – Load Initial Dataset

The Day 1 CSV file was loaded into PostgreSQL:

```sql
\copy sensor_readings(id, name, age, reading_date)
FROM '/home/dataops1/linux-exercises/etl_pipeline/exercise_25/sensor_data_day1.csv'
DELIMITER ','
CSV HEADER;
```

## Purpose

This represented the first batch of data received by the system.

The database now contained:

```
1 - Gideon
2 - Ama
3 - Kofi
4 - Abena
5 - Kojo
```

The load was verified using:

```sql
SELECT COUNT(*) FROM sensor_readings;
```

Result:

```
5 records
```

---

# Step 3 – Create Staging Table

A temporary staging table was created:

```sql
CREATE TEMP TABLE sensor_stage (
    id INTEGER,
    name VARCHAR(100),
    age NUMERIC,
    reading_date DATE
);
```

## Purpose

The staging table provided a temporary location where incoming Day 2 data could be inspected before inserting it into the main table.

---

# Step 4 – Load Day 2 Data into Staging Table

The second CSV file was loaded:

```sql
\copy sensor_stage(id, name, age, reading_date)
FROM '/home/dataops1/linux-exercises/etl_pipeline/exercise_25/sensor_data_day2.csv'
DELIMITER ','
CSV HEADER;
```

The staging table contained:

```
4 - Abena
5 - Kojo
6 - Akua
7 - Yaw
8 - Esi
```

---

# Step 5 – Perform Incremental Load

Only new records were inserted into the production table:

```sql
INSERT INTO sensor_readings(id, name, age, reading_date)
SELECT id, name, age, reading_date
FROM sensor_stage
WHERE id NOT IN (
    SELECT id FROM sensor_readings
);
```

## Explanation

The query compared records in `sensor_stage` against existing records in `sensor_readings`.

Existing records:

```
1,2,3,4,5
```

Incoming records:

```
4,5,6,7,8
```

Processing result:

```
4 → Duplicate (Skipped)
5 → Duplicate (Skipped)
6 → New Record (Inserted)
7 → New Record (Inserted)
8 → New Record (Inserted)
```

Output:

```
INSERT 0 3
```

This confirmed that three new records were added.

---

# Step 6 – Verify Final Load

The total number of records was checked:

```sql
SELECT COUNT(*) FROM sensor_readings;
```

Result:

```
8
```

The final data was displayed:

```sql
SELECT * FROM sensor_readings;
```

Final table:

```
id | name
---------
1  | Gideon
2  | Ama
3  | Kofi
4  | Abena
5  | Kojo
6  | Akua
7  | Yaw
8  | Esi
```

---

# Real-World Application

Incremental loading is widely used in professional data engineering systems such as:

* Banking transaction pipelines
* IoT data platforms
* Customer analytics systems
* Data warehouses
* Cloud ETL pipelines

For example, an IoT company receiving millions of sensor readings daily does not reload the entire database. Instead, it processes only the latest sensor records received since the previous load.

---

# Lessons Learned

Through this exercise, the following concepts were practiced:

* Initial data loading
* Incremental ETL processing
* PostgreSQL data ingestion
* Staging table usage
* Duplicate detection
* Efficient database updates

---

# Conclusion

Exercise 25 successfully implemented an incremental ETL loading process using PostgreSQL.

The workflow demonstrated how professional data engineers design efficient pipelines by loading only new records while protecting databases from duplicate data.

This approach improves scalability, performance, and reliability when handling large volumes of continuously generated data.
