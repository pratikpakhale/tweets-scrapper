import json
import uuid

# Load the JSON data
with open('results/formatted_data.json', 'r') as file:
    data = json.load(file)

# Add unique IDs and store as key-value pairs

for key, element in data.items():
    try:
        if element['sentiment'] or element['emotion'] == 0:
            data[key]['tweet'] = {
                "sentiment": element['sentiment'],
                "emotion": element['emotion']
            }
            data[key]['players'] = []
            data[key].pop('sentiment')
            data[key].pop('emotion')
            print(key)
        try:
            if not element['players']:
                data[key]['players']  = []
            print(key)
        except:
            print(key)
            data[key]['players']  = []
    except:
        pass   


# Write the result to a new JSON file
with open('results/formatted_data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)
