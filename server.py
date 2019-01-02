"""
Written by Gabriel Brown
"""
from flask import Flask, render_template, make_response, request

app = Flask(__name__)


# Routes
@app.route("/")
def index():
    return app.send_static_file("index.html")
    #return render_template("index.html")

if __name__ == "__main__":
    # debug mode makes changes instantly visible
    app.run(debug=True)