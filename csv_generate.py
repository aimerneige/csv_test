import os
import csv
import random
import string
from os import path

def random_string_generate(length: int) -> str:
    if length <= 0:
        length = 16
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))

def random_mark() -> str:
    return random.choices(["A", "B", "C", "D", "E", "F"])[0]

cwd = os.getcwd()
csv_out_file_name = "sample.csv"
csv_file_path = path.join(cwd, csv_out_file_name)

with open(csv_file_path, 'w') as f:
    csv_writer = csv.writer(f, delimiter=',', quotechar="\"", quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(["spam", "mark"])
    for i in range(0, 100):
        csv_writer.writerow([random_string_generate(32), random_mark()])
    csv_writer.writerow([random_string_generate(16)+"\n"+random_string_generate(16),random_mark()])
    csv_writer.writerow([random_string_generate(16)+","+random_string_generate(16),random_mark()])
    csv_writer.writerow([random_string_generate(16)+"\"\"\""+random_string_generate(16),random_mark()])