import os
import csv
import uvicorn
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return "Hello, World! Welcome to your Python web app."

@app.route("/about")
def about():
    return "This is your daily bat selection website."


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=10000)
#with open('Dataset1.csv', newline='')as csvfile:
 # batreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
