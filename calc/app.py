# Put your app in here.
from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route("/add")
def render_add_page():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(add(a, b))