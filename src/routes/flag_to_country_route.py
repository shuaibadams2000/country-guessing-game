from flask import request, render_template, Blueprint, flash, redirect, url_for
from src.app.flag_to_country_utils import FlagToCountryUtils
from pandas import read_csv

country_from_flag_bp = Blueprint('country_from_flag', __name__, template_folder='templates')

flag_to_country_utils = FlagToCountryUtils(read_csv("static/data/countries.csv"))
all_countries = flag_to_country_utils.get_all_countries_in_continent("africa")
all_countries = flag_to_country_utils.randomise_countries(all_countries)
list_of_countries = flag_to_country_utils.to_list(all_countries)

country_name = list_of_countries[0].CountryName
flag_path = flag_to_country_utils.get_country_flag_path(country_name)

@country_from_flag_bp.route('/country-from-flag', methods=["GET", "POST"])
def country_from_flag():
    global flag_path, country_name

    if request.method == "POST":
        country_name_input = request.form.get("country-name-input")
        print(f"Country name entered: {country_name_input.lower()}")
        if list_of_countries:
            if flag_to_country_utils.is_guess_correct(country_name_input, country_name):
                # Move on to the next country
                print("Answered correctly")
                country_name = list_of_countries.pop().CountryName
                flag_path = flag_to_country_utils.get_country_flag_path(country_name)
            else:
                print("Answered incorrectly")
        return redirect(url_for('country_from_flag.country_from_flag'))

    return render_template("country_from_flag.html", flag_path=flag_path)
