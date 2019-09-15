from flask import Flask
from library import *

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! the result is <b>" + str(sum_val(4,3)) + "</b>."

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
