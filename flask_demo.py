from flask import Flask, render_template, jsonify
import jinja2
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "ASDFKN"
app.config["JSON_AS_ASCII"] = False

debug_data = {"name": "终成硕", "pwd": "keji", }

@app.route("/")
def haha():
    return render_template("hehe.html", data=debug_data)

@app.route("/hope", methods=["GET", "POST"])
def test():
    return render_template("hope.html")

if __name__ == '__main__':
    app.run("127.0.0.1", 666)