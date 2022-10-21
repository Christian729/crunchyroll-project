from flask_app import app

from flask import render_template, redirect

from flask_app.models.user import User

# ----------------------One of the first things we want to do when rendering a new project is setting up routes-------------------
@app.route('/')
def index():
    return render_template('index.html')