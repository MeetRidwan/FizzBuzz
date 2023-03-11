from flask import Flask, render_template, request

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/fizzbuzz")
def fizzbuzz():
    return render_template("fizzbuzz.html")

