from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')  # sets up the route of the app
@app.route('/jobs') # makes the jobs function reachable

def jobs():
    return render_template('index.html')  # rendes index.html
