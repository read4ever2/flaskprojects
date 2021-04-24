from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return show_hello()


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form["username"]


        password = request.form["password"]
        error = None
        if not username:
            error = "Username is required."

        elif not password:
            error = "Password is required."
        flash(error)
        # TODO: Encrypt and Store credentials
        if error == None:
            return redirect(url_for("hello"))
    return render_template('register.html')


# Can call functions as part of the returns
def show_hello():
    return 'Hello, UMGC SDEV Students!'


# Can provide multiple route versions
# And can render template - found in /template folder
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
