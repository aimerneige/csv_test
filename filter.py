import os
import csv
import json
from os import path

cwd_path = os.getcwd()
source_file_name = "sample.csv"
source_file_path = path.join(cwd_path, source_file_name)
source_file = open(source_file_path, "r")
csv_reader = csv.reader(
    source_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
)
next(csv_reader, None)  # skip header
header = ["spam", "mark"]

dict_file_name = "dict_data.json"
dict_file_path = path.join(cwd_path, dict_file_name)
dict_file = open(dict_file_path, 'w')
dict_data = {
    "A": [],
    "B": [],
    "C": [],
    "D": [],
    "E": [],
    "F": [],
}
for row in csv_reader:
    spam = row[0]
    mark = row[1]
    dict_data[mark].append(spam)
json.dump(dict_data, dict_file, ensure_ascii=False)

source_file.close()
dict_file.close()
