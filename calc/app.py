# Put your app in here.
from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route("/add")
def render_add_page():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(add(a, b))

@app.route("/sub")
def render_sub_page():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(sub(a, b))

@app.route("/mult")
def render_mult_page():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(mult(a, b))

@app.route("/div")
def render_div_page():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(div(a, b))

@app.route("/math/<operation>")
def render_math_page(operation):
    a = int(request.args["a"])
    b = int(request.args["b"])
    operations = {"add": add, "sub": sub, "mult": mult, "div": div}
    return str(operations[operation](a, b))