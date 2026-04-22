from flask import Flask, Blueprint, render_template, request, url_for, redirect

home_bp = Blueprint('home', __name__, template_folder='templates')


@home_bp.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print("Play button clicked!")
        return redirect(url_for("continent_selector"))
    return render_template("index.html")
