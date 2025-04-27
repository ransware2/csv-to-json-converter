import csv
import json
import sys
import os

def csv_to_json(csv_filepath, json_filepath):
    data = []
    with open(csv_filepath, encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    
    with open(json_filepath, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

    print(f"Success! JSON file saved at {json_filepath}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py input.csv output.json")
    else:
        input_csv = sys.argv[1]
        output_json = sys.argv[2]
        if not os.path.exists(input_csv):
            print(f"Error: File {input_csv} does not exist.")
        else:
            csv_to_json(input_csv, output_json)
