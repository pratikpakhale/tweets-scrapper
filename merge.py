import os
import json

# Function to read JSON from a file
def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Function to write JSON to a file
def write_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Function to merge JSON arrays
def merge_json_arrays(array1, array2):
    return array1 + array2

# Directory containing JSON files
directory = '/home/pratz/Desktop/Projects Archive/Tweets Scrapper'

# List to store merged data
merged_data = []

# Loop through files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        file_path = os.path.join(directory, filename)
        # Read JSON from file
        json_data = read_json(file_path)
        # Merge JSON arrays
        merged_data = merge_json_arrays(merged_data, json_data)

# Calculate the length of the merged array
merged_array_length = len(merged_data)
print("Length of merged array:", merged_array_length)

# Write merged data to ALL.json
write_json('ALL.json', merged_data)
