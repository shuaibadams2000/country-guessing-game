from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/country-from-flag')
def country_from_flag():
    return render_template("country_from_flag.html")

if __name__ == '__main__':
    app.run(debug=True)
