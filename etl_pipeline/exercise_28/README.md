# Exercise 28 – ETL Automation Using Bash

## Overview

This exercise demonstrates how to automate an ETL (Extract, Transform, Load) pipeline using a Bash shell script. Instead of manually executing each step of the ETL process, a single automation script performs the entire workflow, making the process faster, more reliable, and repeatable.

The automation script performs the following tasks:

* Simulates downloading a CSV file.
* Executes a Python ETL transformation script.
* Archives the processed source file.
* Records the execution process in a log file.

This approach reflects how production ETL pipelines are automated in real-world data engineering environments.

---

# Exercise Objectives

By completing this exercise, the following objectives were achieved:

* Understand the purpose of ETL automation.
* Create a Bash script to automate an ETL workflow.
* Simulate downloading a source CSV file.
* Execute a Python transformation script automatically.
* Archive processed source files.
* Record ETL execution events in a log file.
* Build a repeatable ETL process suitable for scheduled execution

---

# ETL Workflow

The automated workflow performs the following sequence of operations:

```text
Incoming CSV
      │
      ▼
Simulate Download
      │
      ▼
Python Transformation
      │
      ▼
Generate Processed Output
      │
      ▼
Archive Original CSV
      │
      ▼
Record Execution Log
```

---

# Automation Process

The Bash script (`etl.sh`) performs the following operations:

1. Records the ETL start time in the log file.
2. Simulates downloading the source CSV by copying it from the `incoming` directory.
3. Executes the Python transformation script.
4. Verifies whether the Python script completed successfully.
5. Archives the processed source CSV using a timestamped filename.
6. Records the completion status in the execution log.

---

# Python Transformation

The Python script (`transform.py`) performs the following transformations:

* Reads the source CSV.
* Converts temperatures from Celsius to Fahrenheit.
* Adds a processing timestamp.
* Generates a new transformed CSV file.

---

# Logging

Every execution is recorded in:

```text
logs/etl.log
```



# Archiving

After a successful ETL run, the original source file is moved into the `archive` directory using a timestamped filename.

Example:

```text
archive/
└── sensor_data_20260722_101234.csv
```

Archiving preserves the original data for auditing, recovery, and historical reference.

---

# Learning Outcomes

This exercise provided practical experience with:

* Bash scripting.
* ETL automation.
* Executing Python scripts from Bash.
* File management in Linux.
* Logging ETL executions.
* Archiving processed datasets.
* Building repeatable and production-style ETL workflows.



# Conclusion

Exercise 28 introduced ETL automation using Bash scripting. By combining Linux shell commands with a Python transformation script, a complete automated workflow was created that downloads data, processes it, archives the original file, and records execution details.

This exercise reinforces the importance of automation, repeatability, and operational reliability in modern data engineering pipelines.
