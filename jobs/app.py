import sqlite3
from flask import Flask, render_template, g

PATH = db/jobs.sqlite

app = Flask(__name__)

def open_connection():
    connection = getatt(g, '_connection', None)
    if connection:
        connection = g._connection =  sqlite3.connect(PATH)
    connetion.row_factory = sqlite3.Row
    return connection


@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
