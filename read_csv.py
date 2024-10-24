import csv
# Define the filename
csv_file_path=r'C:\Users\M Adithya\Downloads\customers-100.csv'

# Read the CSV file
with open(csv_file_path,mode='r') as csvfile:
    csv_reader = csv.reader(csvfile)

    # Read each row
    for row in csv_reader:
        print("Row:", row)