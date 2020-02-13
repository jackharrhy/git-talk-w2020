from flask import Flask
app = Flask(__name__)

@app.route('/')
def go_world():
    return 'Go, World!'
