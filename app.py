# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
from model import getImageUrlFrom
import os

# -- Initialization section --
app = Flask(__name__)

app.config['GIPHY_KEY'] = os.getenv("GIPHY_KEY")

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time = datetime.now())

@app.route('/yourgif', methods = ['GET', 'POST'])
def getgif():
    user_input = request.form['gifchoice']
    print(user_input)
    source = getImageUrlFrom(user_input, app.config['GIPHY_KEY'])
    return render_template('yourgif.html', pic = source)
