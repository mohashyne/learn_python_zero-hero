import csv


# What is CSV?

# CSV stands for Comma-Separated Values. It is a file format used to store tabular data, such as spreadsheets or databases, in plain text. Each line in a CSV file represents a row, and the values in the row are separated by a delimiter, commonly a comma (,). Other delimiters like tabs, semicolons, or pipes can also be used.
# Example of a CSV file:

# Name,Age,City
# Alice,30,New York
# Bob,25,Los Angeles
# Charlie,35,Chicago



# Data to write to the CSV
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

# file =  open("data.csv", "w")
# file.close

# or

# Open the file in write mode and write the data
with open("Section-3/13-create_csv_file/data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
    
    
    # manual writer
    # writer.writerow(["Name", "Age", "City"])
    # writer.writerow(["Alice", 30, "New York"])
    # writer.writerow(["Bob", 25, "Los Angeles"])
    # writer.writerow(["Charlie", 35, "Chicago"])


# How to open an existing csv file
with open("Section-3/13-create_csv_file/data.csv", "r") as file:
    reader = csv.reader(file)
    # print(list(reader)) 
            # or
    for row in reader:
        print(row)  # prints each row as a list of values
        
        
# print(row[0])  # prints the first value in each row
# print(row[1])  # prints the second value in each row
# print(row[2])  # prints the third value in each row
# print(row[3])  # prints the fourth value in each row
# print(row[4])  # prints the fifth value in each row
    
        
