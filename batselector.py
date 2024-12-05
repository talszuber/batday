const port = process.env.PORT || 4000
import csv
with open('Dataset1.csv', newline='')as csvfile:
  batreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
