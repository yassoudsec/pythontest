from flask import Flask
from library import *

app = Flask(__name__)

@app.route("/")
def hello():
    return "La somme de a et b est <b>" + str(sum_val(4,3)) + "</b>."

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
