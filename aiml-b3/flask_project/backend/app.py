from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello_world():
    return "Hello Aiml B3"

@app.route("/mobiles")
def mobiles():
    return "mobile list"

