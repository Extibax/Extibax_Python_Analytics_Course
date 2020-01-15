""" Modules """
from flask import Flask, render_template
from scripts.rup import Rup

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    print("Server on port 5000")
    app.run(debug=True)
