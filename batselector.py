import os
import csv
port = int(os.environ.get('PORT', 1000))
with open('Dataset1.csv', newline='')as csvfile:
  batreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
