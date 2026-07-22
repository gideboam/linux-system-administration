# Exercise 29 – ETL Scheduling Using Cron

## Overview

This exercise demonstrates how to automate the execution of an ETL pipeline using the Linux Cron scheduler. Rather than manually running the ETL process, Cron executes the ETL script automatically at fixed time intervals.

The objective of this exercise was to configure a scheduled task that runs an ETL script every 15 minutes and verify that each execution is successfully recorded in a log file.

This exercise builds upon the ETL automation developed in the previous exercise by introducing task scheduling, a critical component of production data engineering.

---

# Exercise Objectives

By completing this exercise, the following objectives were achieved:

* Understand the concept of task scheduling.
* Learn how the Linux Cron service works.
* Create a scheduled Cron job.
* Configure an ETL script to execute every 15 minutes.
* Verify scheduled executions using log files.
* Understand the relationship between automation and scheduling.
* Simulate how production ETL pipelines are executed automatically.

---

# Technologies Used

* Linux
* Bash Shell
* Cron
* Shell Scripting
* Linux File System

---

# Project Structure

```text
exercise_29/
│
├── etl.sh
├── logs/
│   └── etl.log
└── README.md
```

---

# Scheduling Workflow

The workflow implemented in this exercise is shown below:

```text
Cron Scheduler
        │
        ▼
Execute etl.sh
        │
        ▼
Record Execution Time
        │
        ▼
Append Log Entry
        │
        ▼
Verify Successful Execution
```

---

# Cron Job Configuration

The following Cron expression was configured:

```cron
*/15 * * * * /home/dataops1/linux-exercises/etl_pipeline/exercise_29/etl.sh
```

This schedule means:

* Every 15 minutes
* Every hour
* Every day of the month
* Every month
* Every day of the week

Cron automatically executes the ETL script without requiring manual intervention.

---

# ETL Script

The ETL script records the execution time of every scheduled run by appending a timestamp to the log file.

Example log entry:

```text
ETL executed at Wed Jul 22 03:45:00 PM CEST 2026
```

Each execution creates a new log entry, making it possible to verify that the scheduler is functioning correctly.

---

# Verification Process

The following steps were used to verify successful scheduling:

1. Created and configured a Cron job.
2. Confirmed the Cron configuration using:

```bash
crontab -l
```

3. Verified that the Cron service was running:

```bash
sudo systemctl status crond
```

4. Waited for the next scheduled execution interval.

5. Checked the execution log:

```bash
cat logs/etl.log
```

A new timestamp confirmed that the scheduled ETL job executed successfully.

---

# Key Learning Outcomes

This exercise provided practical experience with:

* Linux Cron scheduling.
* Scheduling automated ETL jobs.
* Managing Cron jobs.
* Verifying scheduled task execution.
* Monitoring ETL execution through log files.
* Understanding production scheduling practices.

---

# Real-World Application

In modern data engineering environments, ETL pipelines are rarely executed manually. Instead, scheduling tools automatically trigger workflows at predefined intervals.

Common examples include:

* Running sales ETL pipelines every night.
* Importing IoT sensor data every 15 minutes.
* Refreshing business intelligence dashboards every hour.
* Performing automated database backups.
* Generating operational reports on scheduled intervals.

Although enterprise environments often use workflow orchestration platforms such as Apache Airflow, Prefect, or cloud-native schedulers, Cron remains one of the most widely used scheduling tools for Linux servers.

---

# Conclusion

Exercise 29 introduced ETL scheduling using the Linux Cron service. A Bash script was scheduled to execute automatically every 15 minutes, and successful executions were verified through timestamped log entries.

This exercise demonstrates how automation and scheduling work together to create reliable, repeatable, and production-ready ETL workflows, providing a strong foundation for more advanced orchestration tools used in enterprise data engineering.
