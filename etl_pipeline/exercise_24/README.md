# Exercise 24 – Database Loading

## Objective

The objective of this exercise is to learn how to load cleaned CSV data into a PostgreSQL database as part of the ETL (Extract, Transform, Load) process. The exercise demonstrates how to create a database table, import structured data from a CSV file, and verify that the data has been loaded successfully.

---

## Learning Outcomes

By completing this exercise, you will be able to:

- Understand the **Load** phase of the ETL pipeline.
- Connect to PostgreSQL using the command-line interface.
- Create a relational database table.
- Verify a table's structure before importing data.
- Import CSV data into PostgreSQL using the `\copy` command.
- Validate imported data using SQL queries.
- Troubleshoot common file permission issues during data loading.

---

## Technologies Used

- PostgreSQL 13
- Linux (Rocky Linux)
- Bash
- SQL
- CSV

---

## Project Structure

```text
exercise_24/
└── README.md

exercise_23/
└── cleaned_data.csv
```

---

## Steps Performed

### 1. Connected to PostgreSQL

Switched to the PostgreSQL system user and opened the PostgreSQL interactive terminal.

```bash
sudo -i -u postgres
psql
```

---

### 2. Created the Database Table

Created a table named **sensor_readings** with the appropriate columns and data types.

```sql
CREATE TABLE sensor_readings (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    age NUMERIC,
    reading_date DATE
);
```

---

### 3. Verified the Table Structure

Displayed the table schema to confirm the columns, data types, and constraints.

```sql
\d sensor_readings
```

---

### 4. Loaded the CSV File

Imported the cleaned CSV generated in Exercise 23 into the PostgreSQL table.

```sql
\copy sensor_readings(id, name, age, reading_date)
FROM '/home/dataops1/linux-exercises/etl_pipeline/exercise_23/cleaned_data.csv'
DELIMITER ','
CSV HEADER;
```

---

### 5. Verified the Number of Records

Confirmed that all records from the CSV file were successfully imported.

```sql
SELECT COUNT(*) FROM sensor_readings;
```

Expected Output:

```text
 count
-------
     8
```

---

### 6. Verified the Imported Data

Displayed all records stored in the table.

```sql
SELECT * FROM sensor_readings;
```

Expected Output:

```text
 id |  name  |        age         | reading_date
----+--------+--------------------+--------------
 1  | Gideon | 27.0               | 2026-07-10
 2  | Ama    | 24.0               | 2026-07-10
 3  | Kofi   | 28.166666666666668 | 2026-07-11
 4  | Abena  | 30.0               | 2026-07-11
 5  | Kojo   | 28.0               | 2026-07-12
 6  | Akua   | 31.0               | 2026-07-12
 7  | Yaw    | 28.166666666666668 | 2026-07-13
 8  | Esi    | 29.0               | 2026-07-13
```

---

## Challenges Encountered

### Peer Authentication Failure

Initially, connecting with:

```bash
psql -U postgres
```

resulted in a peer authentication error because PostgreSQL uses Linux user authentication by default.

This was resolved by switching to the PostgreSQL system account:

```bash
sudo -i -u postgres
```

---

### Permission Denied While Importing CSV

During the `\copy` operation, PostgreSQL could not access the CSV file because the `postgres` user did not have execute permission on the `/home/dataops1` directory.

This was resolved by allowing directory traversal:

```bash
chmod o+x /home/dataops1
```

After updating the directory permission, the CSV file imported successfully.

---

## Key SQL Commands Learned

| Command | Purpose |
|----------|---------|
| `CREATE TABLE` | Creates a new database table. |
| `\d table_name` | Displays the table structure. |
| `\copy` | Imports CSV data into a PostgreSQL table. |
| `SELECT COUNT(*)` | Counts the total number of records. |
| `SELECT *` | Displays all rows stored in a table. |
| `\q` | Exits the PostgreSQL terminal. |

---

## ETL Pipeline Overview

```text
Dirty CSV
      │
      ▼
Exercise 23
(Python Data Cleaning)
      │
      ▼
cleaned_data.csv
      │
      ▼
Exercise 24
(PostgreSQL Database Loading)
      │
      ▼
sensor_readings Table
      │
      ▼
Validation
(Row Count & Data Verification)
```

---

## Real-World Relevance

In modern data engineering pipelines, raw data is first cleaned and standardized before being loaded into a database. This ensures that downstream applications, dashboards, analytics platforms, and machine learning systems work with accurate and consistent data.

The workflow implemented in this exercise reflects a common production ETL process used in industries such as finance, healthcare, telecommunications, logistics, and cloud-based data platforms.

---

## Conclusion

This exercise demonstrated the complete **Load** phase of the ETL process by importing a cleaned CSV file into a PostgreSQL database. The exercise covered database table creation, schema verification, CSV data loading, record validation, and troubleshooting Linux file permission issues. These are essential practical skills for building reliable and production-ready data engineering pipelines.
