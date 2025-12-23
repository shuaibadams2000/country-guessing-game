from operator import index

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import pandas

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    return render_template("index.html")

# @app.route('/country-from-flag', methods=["GET", "POST"])
# def country_from_flag():
#     if request.method == "POST":
#         country_name_input = request.form.get("country-name-input")
#         print(country_name_input)
#     return render_template("country_from_flag.html")
#
# if __name__ == '__main__':
#     app.run(debug=True)
