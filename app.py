from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def default_route():
    return hello()


@app.route("/hello")
def hello():
    return "Hello World!"


@app.route("/add", methods=['POST'])
def add():
    app.logger.warn("Received request:" + str(request.json))
    return {
        "result": request.json['value1'] + request.json['value2']
    }