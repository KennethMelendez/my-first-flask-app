# views.py

from flask import render_template

# Flask provides a method, render_template, which we can use to specifiy which HTML file should be loaded in a particular view.

from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")    
    