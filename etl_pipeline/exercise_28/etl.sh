#!/bin/bash

echo "========== ETL Started: $(date) ==========" >> logs/etl.log

# Simulate downloading the CSV
cp incoming/sensor_data.csv sensor_data.csv
echo "$(date): CSV downloaded successfully." >> logs/etl.log

# Run the Python ETL
python3 transform.py

if [ $? -eq 0 ]; then
    echo "$(date): Python ETL completed successfully." >> logs/etl.log

    # Archive the processed CSV
    mv sensor_data.csv archive/sensor_data_$(date +%Y%m%d_%H%M%S).csv
    echo "$(date): Source file archived." >> logs/etl.log
else
    echo "$(date): Python ETL failed." >> logs/etl.log
fi

echo "========== ETL Finished: $(date) ==========" >> logs/etl.log
