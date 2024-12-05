import os
import csv
port = int(os.environ.get('PORT', '0.0.0.0:8080'))
with open('Dataset1.csv', newline='')as csvfile:
  batreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
