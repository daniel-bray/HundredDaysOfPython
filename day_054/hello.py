# activate env '. venv/bin/activate' then 'python3 -m flask run'

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, world"


@app.route("/home")
def main_page():
    return "this is the home page"


if __name__ == "__main__":
    app.run()
