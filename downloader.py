import csv
import os

current_dir = os.getcwd()

with open(current_dir+"/pdf_links.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

