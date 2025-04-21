import csv
# Data to be written to the CSV file
data = [
    {"user_name": "Kazhymukan", "phone_number": "+77477634745"},
    {"user_name": "Azim", "phone_number": "+77751016593"},
    {"user_name": "Sanzhar", "phone_number": "+77079411524"}
]

# Path to the CSV file
csv_file_path = "pb.csv"

# Write data to the CSV file
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    
    # Write header
    writer.writeheader()
    
    # Write data rows
    for row in data:
        writer.writerow(row)