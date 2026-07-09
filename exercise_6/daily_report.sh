#!/bin/bash

echo "===== Daily System Report =====" >> daily_report.log
date >> daily_report.log
echo "" >> daily_report.log

echo "Memory Usage:" >> daily_report.log
free -h >> daily_report.log
echo "" >> daily_report.log

echo "Disk Usage:" >> daily_report.log
df -h >> daily_report.log
echo "" >> daily_report.log

echo "==============================" >> daily_report.log
echo "" >> daily_report.log
