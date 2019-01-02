# Made by Gabriel Brown

from flask import Flask, render_template, make_response, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world!"

if __name__ == "__main__":
    # debug mode makes changes instantly visible
    app.run(debug=True)