from flask import Flask
app = Flask(__name__)

@app.route('/')
def bye_world():
    return 'bye, World!'
