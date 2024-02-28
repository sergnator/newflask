import flask
from flask import Flask, render_template
import multiprocessing
app = Flask(__name__)


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return '3'


@app.route('/registration')
def registration():
    return '3'


@app.route('/posts')
def posts():
    return '3'


a = multiprocessing.Process(target=app.run)
a.start()

