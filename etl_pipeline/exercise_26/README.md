# Exercise 26 – Data Transformation

## Overview

This exercise focuses on the **Transformation** stage of the ETL (Extract, Transform, Load) process. Data transformation involves converting raw data into a format that is suitable for analysis, reporting, or storage in a destination system.

In this exercise, a CSV file containing temperature readings in **Celsius** was processed using Python. Each temperature value was converted to **Fahrenheit**, and a **processing timestamp** was added to every record. The transformed data was then saved into a new CSV file, preserving the original dataset.

This exercise demonstrates how data engineers modify incoming data to satisfy business requirements before it is loaded into a database or data warehouse.

---

# Exercise Objectives

The objectives of this exercise were to:

1. Understand the Transformation stage of an ETL pipeline.
2. Read data from a CSV file using Python and Pandas.
3. Convert temperature values from Celsius (°C) to Fahrenheit (°F).
4. Add a processing timestamp to every record.
5. Save the transformed data into a new CSV file.
6. Verify the transformed output before loading it into a database.

---

# Technologies Used

* Python 3
* Pandas
* CSV Files
* Linux Command Line
* ETL Concepts

---

# Key Definitions

## Transformation

Transformation is the second phase of the ETL process where extracted data is modified into the required format before it is loaded into a destination system.

Typical transformations include:

* Converting measurement units
* Standardizing date formats
* Creating calculated columns
* Renaming fields
* Filtering unwanted records
* Cleaning inconsistent values

---

## Celsius (°C)

Celsius is the temperature scale commonly used in most countries around the world.

Examples:

* Water freezes at **0°C**
* Water boils at **100°C**

---

## Fahrenheit (°F)

Fahrenheit is another temperature scale primarily used in the United States and a few other countries.

Examples:

* Water freezes at **32°F**
* Water boils at **212°F**

The conversion formula is:

```text
°F = (°C × 9/5) + 32
```

---

## Timestamp

A timestamp records the exact date and time when an event occurs.

In ETL pipelines, timestamps help identify:

* when data was processed,
* when it was transformed,
* when it was loaded into a system.

---

# Project Structure

```text
exercise_26/
│
├── temperatures.csv
├── transform.py
├── transformed_temperatures.csv
└── README.md
```

---

# Workflow

The transformation process followed these steps:

```text
Raw CSV Data
      │
      ▼
Read CSV using Pandas
      │
      ▼
Convert Celsius to Fahrenheit
      │
      ▼
Add Processing Timestamp
      │
      ▼
Save Transformed CSV
      │
      ▼
Verify Output
```

---

# Python Transformation Process

The transformation script performed the following operations:

### 1. Read the Source File

The script loaded the raw CSV data into a Pandas DataFrame.

### 2. Convert Temperature Units

A new column named `temperature_f` was created using the formula:

```text
°F = (°C × 9/5) + 32
```

The original Celsius values were preserved.

### 3. Add Processing Timestamp

A new column named `processed_timestamp` was generated using Python's `datetime` module.

Each record received the exact date and time when the transformation was executed.

### 4. Save the Transformed Data

The transformed dataset was exported to:

```text
transformed_temperatures.csv
```

The original input file remained unchanged.

---

# Sample Output

| ID | Location | Temperature (°C) | Temperature (°F) |
| -- | -------- | ---------------: | ---------------: |
| 1  | Accra    |             30.0 |             86.0 |
| 2  | Kumasi   |             28.0 |             82.4 |
| 3  | Takoradi |             31.0 |             87.8 |
| 4  | Tamale   |             35.0 |             95.0 |
| 5  | Ho       |             27.0 |             80.6 |

Each record also included a `processed_timestamp` indicating when the transformation occurred.

---

# Real-World Application

Data transformation is one of the most common tasks performed by data engineers.

Examples include:

* Converting temperatures for international weather applications.
* Converting currencies for global financial systems.
* Standardizing dates from multiple countries.
* Calculating sales tax or discounts before reporting.
* Formatting customer data before loading into a data warehouse.

In this exercise, the ETL pipeline automatically converted temperatures from Celsius to Fahrenheit and recorded the processing time, ensuring the data met downstream business requirements.

---

# Lessons Learned

Through this exercise, the following concepts were practiced:

* Reading CSV files with Pandas.
* Performing mathematical transformations on data.
* Creating new calculated columns.
* Adding timestamps for auditability.
* Writing transformed data to a new CSV file.
* Preserving the original source data while generating transformed output.

---

# Conclusion

Exercise 26 demonstrated the Transformation phase of the ETL process using Python and Pandas.

By converting temperatures from Celsius to Fahrenheit and appending processing timestamps, the exercise illustrated how raw data can be enriched and standardized before being loaded into a destination system.

This workflow reflects a common practice in professional data engineering, where transformed datasets improve consistency, support business requirements, and ensure reliable downstream analytics.
