import csv
import json


def csv_to_json(csv_file, json_file):
    # Using utf-8-sig to remove BOM
    with open(csv_file, mode="r", encoding="utf-8-sig") as file:
        csv_reader = csv.DictReader(file)
        data = [line for line in csv_reader]

    with open(json_file, mode="w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


csv_file = "csv_file.csv"
json_file = "json_file.json"
csv_to_json(csv_file, json_file)
