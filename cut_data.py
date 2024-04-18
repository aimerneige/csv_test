import os
import csv
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
for skip in range(0, 20):  # skip to 20
    next(csv_reader, None)

cut_file_name = "cut_data.csv"
cut_file_path = path.join(cwd_path, cut_file_name)
cut_file = open(cut_file_path, "w")
csv_writer = csv.writer(
    cut_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
)
csv_writer.writerow(header)

counter = 0
for row in  csv_reader:
    counter += 1
    if counter > 30:
        break
    csv_writer.writerow(row)

source_file.close()
cut_file.close()