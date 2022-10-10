from flask import Flask

app = Flask(__name__)


@app.route("/")
def default_route():
    return hello()


@app.route("/hello")
def hello():
    return "Hello World!"