# Exercise 6 – Scheduling Jobs (Cron Automation)

## Objective

The objective of this exercise was to learn how to automate repetitive tasks in Linux using **cron jobs**. A script was created to collect important system information, including the current date, memory usage, and disk usage, and save the results into a log file called `daily_report.log`.

The script was then scheduled using `crontab` to execute automatically every five minutes.

This exercise introduced the importance of task automation in Linux environments, which is widely used in DevOps, Data Engineering, System Administration, and Site Reliability Engineering (SRE).

---

# Tasks Completed

The following tasks were completed:

* Created a Bash script to generate a daily system report.
* Collected:

  * Current date and time.
  * Current memory usage.
  * Current disk usage.
* Redirected output into a log file.
* Granted execution permission to the script.
* Tested the script manually.
* Created a cron job to execute the script every five minutes.
* Verified the cron schedule.

---

# Script Creation

A Bash script named:

```bash
daily_report.sh
```

was created to automate system monitoring.

The script contains:

```bash
#!/bin/bash

echo "===== Daily System Report =====" >> daily_report.log
date >> daily_report.log

echo "Memory Usage:" >> daily_report.log
free -h >> daily_report.log

echo "Disk Usage:" >> daily_report.log
df -h >> daily_report.log

echo "==============================" >> daily_report.log
```

---

# Explanation of Script Commands

## Shebang

```bash
#!/bin/bash
```

The shebang tells Linux that the script should be executed using the Bash shell interpreter.

---

## Date Command

```bash
date >> daily_report.log
```

The `date` command displays the current system date and time.

The `>>` operator appends the output to `daily_report.log` without deleting previous records.

---

## Memory Usage

```bash
free -h >> daily_report.log
```

The `free` command displays information about system memory usage.

The `-h` option means "human-readable", making the output easier to understand by displaying values in units such as MB and GB.

Example:

```text
Mem: 11Gi total 3.5Gi used
```

---

## Disk Usage

```bash
df -h >> daily_report.log
```

The `df` command displays disk space usage for mounted filesystems.

The `-h` option formats the output into a human-readable format.

Example:

```text
Filesystem   Size   Used   Avail
/dev/sda4    199G   15G    185G
```

---

# Making the Script Executable

Initially, the script was only a text file. Linux requires execute permission before a script can be run directly.

The following command was used:

```bash
chmod +x daily_report.sh
```

Explanation:

* `chmod` → Change file permissions.
* `+x` → Add execute permission.
* `daily_report.sh` → The file receiving the permission.

The permission was verified using:

```bash
ls -l
```

Output:

```text
-rwxr-xr-x daily_report.sh
```

The presence of `x` confirms that the file is executable.

---

# Testing the Script Manually

Before scheduling the script, it was tested manually:

```bash
./daily_report.sh
```

The `./` tells Linux to execute the script located in the current directory.

After execution, the generated report was verified using:

```bash
cat daily_report.log
```

The log file successfully displayed:

* Date and time.
* Memory usage.
* Disk usage.

---

# Scheduling the Script Using Cron

Cron is a Linux scheduling service used to automate repetitive tasks.

The cron table was edited using:

```bash
crontab -e
```

The following cron job was added:

```bash
*/5 * * * * /home/dataops1/exercise_6/daily_report.sh
```

---

# Understanding the Cron Expression

Cron uses five fields to determine when a job should run.

```text
*/5 * * * * command
│   │ │ │ │
│   │ │ │ └── Day of week
│   │ │ └──── Month
│   │ └────── Day of month
│   └──────── Hour
└──────────── Minute
```

Explanation:

```text
*/5
```

Runs the script every five minutes.

The remaining `*` values mean:

* Every hour.
* Every day.
* Every month.
* Every day of the week.

---

# Verifying the Cron Job

The installed cron jobs were checked using:

```bash
crontab -l
```

Output:

```text
*/5 * * * * /home/dataops1/exercise_6/daily_report.sh
```

This confirmed that the scheduled task was successfully configured.

---

# Key Concepts Learned

## Automation

Automation reduces manual work by allowing Linux to execute repetitive tasks automatically.

## Cron

Cron is a Linux scheduler used for running scripts or commands at specific times.

## File Permissions

Linux requires execute permission before scripts can be run directly.

## Output Redirection

The difference between:

```bash
>
```

and

```bash
>>
```

was practiced.

* `>` overwrites existing content.
* `>>` appends new content while preserving previous data.

## Absolute Paths

Cron jobs should use absolute paths because cron runs in a limited environment and may not know the user's current directory.

Example:

Correct:

```bash
/home/dataops1/exercise_6/daily_report.sh
```

Instead of:

```bash
daily_report.sh
```

---

# Outcome

This exercise provided practical experience in Linux automation by creating a monitoring script and scheduling it with cron. The skills learned are important for managing production systems, monitoring servers, automating ETL tasks, generating reports, and maintaining reliable data pipelines.

The completed workflow was:

```
Create Script
      |
      ↓
Add Commands
      |
      ↓
Grant Execute Permission
      |
      ↓
Test Manually
      |
      ↓
Schedule with Cron
      |
      ↓
Verify Automated Execution
```

Exercise 6 successfully demonstrated how Linux administrators and engineers automate routine operational tasks.
