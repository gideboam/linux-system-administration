# Exercise 27 – ETL Error Handling

## Overview

This exercise focuses on improving the reliability and robustness of an ETL (Extract, Transform, Load) pipeline by implementing **error handling mechanisms**.

In real-world data engineering environments, incoming data is often incomplete, inconsistent, or corrupted. A production ETL pipeline must be designed to handle these situations without completely failing. Instead of stopping when an error occurs, the pipeline should identify invalid records, skip them, record the errors, and continue processing valid data.

In this exercise, a Python-based ETL pipeline was modified to:

* Detect invalid sensor records.
* Skip records containing errors.
* Log error details for investigation.
* Continue processing valid records.
* Generate a clean output dataset.

---

# Exercise Objectives

The objectives of this exercise were to:

1. Understand the importance of error handling in ETL pipelines.
2. Identify invalid records during data processing.
3. Skip corrupted or incomplete records without stopping execution.
4. Generate error logs for rejected records.
5. Produce a cleaned dataset containing only valid records.
6. Build a more reliable and production-ready ETL workflow.

---

# Technologies Used

* Python 3
* CSV Module
* Linux Command Line
* ETL Concepts
* File Handling

---

# Key Definitions

## Error Handling

Error handling is the process of detecting, managing, and responding to unexpected problems during program execution.

In ETL pipelines, error handling ensures that a single bad record does not stop the entire data processing workflow.

---

## Bad Record

A bad record is a data entry that does not satisfy the required validation rules.

Examples include:

* Missing required fields.
* Invalid data types.
* Incorrect formatting.
* Corrupted values.

Example:

```csv
5,Tamale,invalid
```

The temperature value cannot be converted into a valid number, making the record unsuitable for processing.

---

## Error Logging

Error logging is the process of recording information about failures or rejected records into a separate file.

Logs help data engineers:

* Investigate data quality problems.
* Identify faulty sources.
* Debug ETL failures.
* Improve future data processing.

---

## Data Validation

Data validation is the process of checking whether incoming data meets predefined quality requirements before processing.

In this exercise, validation checks included:

* Confirming that location values exist.
* Confirming that temperature values are numeric.

---

# Project Structure

```
exercise_27/
│
├── sensor_data.csv
├── etl_error_handling.py
├── cleaned_data.csv
├── error_log.txt
└── README.md
```

---

# ETL Workflow

The pipeline follows this process:

```
Raw Sensor Data
        |
        ↓
Read CSV File
        |
        ↓
Validate Records
        |
        ├───────────────┐
        |               |
        ↓               ↓
Valid Records       Invalid Records
        |               |
        ↓               ↓
cleaned_data.csv    error_log.txt
```

---

# Input Data

The input file `sensor_data.csv` contained both valid and invalid sensor records.

Example:

```csv
id,location,temperature_c
1,Accra,30
4,,35
5,Tamale,invalid
```

The dataset intentionally included errors to test the pipeline's ability to handle unexpected data.

---

# ETL Processing Logic

The Python script performed the following operations:

## 1. Read Input Data

The CSV file was loaded and processed row by row.

---

## 2. Validate Records

Each record was checked for:

* Missing location values.
* Invalid temperature values.

---

## 3. Process Valid Records

Records that passed validation were written into:

```
cleaned_data.csv
```

Example:

```csv
id,location,temperature_c
1,Accra,30
2,Kumasi,28
3,Takoradi,31
```

---

## 4. Handle Invalid Records

Invalid records were skipped and written into:

```
error_log.txt
```

Example:

```
Skipped record 4: Missing location
Skipped record 5: could not convert string to float: 'invalid'
Skipped record 7: Missing location
```

---

# Error Handling Implementation

The pipeline uses Python exception handling:

```python
try:
    validate_record()

except Exception:
    log_error()
```

The `try` block contains operations that may fail, while the `except` block captures errors and prevents the program from crashing.

---

# Real-World Application

Error handling is a critical feature in professional data engineering systems.

Examples include:

## Banking Systems

Millions of transactions are processed daily. A few corrupted transactions should not stop the entire pipeline.

---

## IoT Systems

Thousands of sensors continuously send data. Some sensors may send incomplete or incorrect readings.

---

## Healthcare Systems

Patient records must be processed reliably while identifying incomplete or invalid information.

---

A production ETL pipeline should:

* Process valid data.
* Isolate bad records.
* Maintain error logs.
* Allow engineers to investigate issues later.

---

# Lessons Learned

Through this exercise, the following concepts were practiced:

* Implementing validation checks in ETL workflows.
* Using Python exception handling.
* Separating valid and invalid data.
* Creating error logs.
* Building fault-tolerant data pipelines.
* Understanding how production systems handle imperfect data.

---

# Conclusion

Exercise 27 demonstrated how error handling improves ETL pipeline reliability.

By skipping bad records, logging errors, and continuing execution, the pipeline becomes more resilient and closer to the standards used in professional data engineering environments.

This approach allows organizations to maintain continuous data processing while ensuring that data quality issues are properly identified and investigated.
