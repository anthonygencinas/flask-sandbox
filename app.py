from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def default_route():
    return hello()


@app.route("/hello")
def hello():
    return "Hello World!\n"


@app.route("/add", methods=['POST'])
def add():
    # Warn message to get message through console
    app.logger.warn("Received request:" + str(request.json))
    return {
        "result": request.json['value1'] + request.json['value2']
    }