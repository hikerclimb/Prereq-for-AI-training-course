import sys
import json

# Ensure the user provided the file name argument
if len(sys.argv) < 2:
    print("Error: Please provide a file name.")
    sys.exit(1)

# Get the filename from the first command-line argument
file_name = sys.argv[1]

with open(file_name, 'r') as file:
    data = json.load(file)

total_amount = 0

with open('FDE_Mini_Challenge_Data_Error_Module2.json', 'w') as error,open('FDE_Mini_Challenge_Data_Successful_Module2.json', 'w') as success:
    for row in data:
        if row['status'] == 'inactive' or row['amount'] < 1000:
            json.dump(row, error)
            error.write("\n")
        else:
            total_amount += row['amount']
            json.dump(row, success)
            success.write("\n")

print(total_amount)
            
            
        
