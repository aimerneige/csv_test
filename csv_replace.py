import os
import csv
from os import path

replace_dic = {
    "A": "1",
    "B": "2",
    "C": "3",
    "D": "4",
    "E": "5",
    "F": "6",
}

cwd = os.getcwd()
csv_in_file_name = "sample.csv"
csv_out_file_name = "replaced.csv"
csv_in_file_path = path.join(cwd, csv_in_file_name)
csv_out_file_path = path.join(cwd, csv_out_file_name)

csv_file_in = open(csv_in_file_path, 'r')
csv_file_out = open(csv_out_file_path, 'w')

csv_reader = csv.reader(csv_file_in, delimiter=',', quotechar="\"", quoting=csv.QUOTE_MINIMAL)
csv_writer = csv.writer(csv_file_out, delimiter=',', quotechar="\"", quoting=csv.QUOTE_MINIMAL)
csv_writer.writerow(["spam", "mark"])
next(csv_reader, None) # skip the header
for row in csv_reader:
    spam = row[0]
    mark = replace_dic[row[1]]
    csv_writer.writerow([spam, mark])

csv_file_in.close()
csv_file_out.close()
