from flask import Flask
app = Flask(__name__)

@app.route('/go')
def go_world():
    return 'Go, World!'

@app.route('/neat')
def neat_world():
    return 'Neat, World!'
