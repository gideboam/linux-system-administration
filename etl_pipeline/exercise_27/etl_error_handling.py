import csv

input_file = "sensor_data.csv"
output_file = "cleaned_data.csv"
error_file = "error_log.txt"

with open(input_file, "r") as file, \
     open(output_file, "w", newline="") as clean_file, \
     open(error_file, "w") as log_file:

    reader = csv.DictReader(file)

    writer = csv.DictWriter(
        clean_file,
        fieldnames=["id", "location", "temperature_c"]
    )

    writer.writeheader()

    for row in reader:
        try:
            if not row["location"]:
                raise ValueError("Missing location")

            float(row["temperature_c"])

            writer.writerow(row)

        except Exception as error:
            log_file.write(
                f"Skipped record {row['id']}: {error}\n"
            )

print("ETL completed successfully")
