import csv
import json

f = open("input.csv", "r")
data = list(csv.DictReader(f))
f.close()

f = open("output.json", "w")
json.dump(data, f, indent=4)
f.close()

print("CSV data converted to JSON successfully!")
