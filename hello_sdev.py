from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return show_hello()


# Can call functions as part of the returns
def show_hello():
    return 'Hello, UMGC SDEV Students!'


# Can provide multiple route versions
# And can render template - found in /template folder
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
