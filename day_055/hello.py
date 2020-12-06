# activate env '. venv/bin/activate' then 'python3 -m flask run'

from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"

    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}</em>"

    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        return f"<u>{function()}</u>"

    return wrapper_function


@app.route("/")
def hello_world():
    return "Hello, world"


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "bye"


@app.route("/<name>")
def greet(name):
    return f"hello {name}"


if __name__ == "__main__":
    app.run(debug=True)
