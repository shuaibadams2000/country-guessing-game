from flask import request, render_template, Blueprint
from src.app.flag_to_country_utils import FlagToCountryUtils
from pandas import read_csv

flag_to_country_utils = FlagToCountryUtils(read_csv("static/data/countries.csv"))

country_from_flag_bp = Blueprint('country_from_flag', __name__, template_folder='templates')

@country_from_flag_bp.route('/country-from-flag', methods=["GET", "POST"])
def country_from_flag():
    if request.method == "POST":
        country_name_input = request.form.get("country-name-input")
        print(country_name_input)

    flag_path = flag_to_country_utils.get_country_flag_path("albania")
    return render_template("country_from_flag.html", flag_path=flag_path)
