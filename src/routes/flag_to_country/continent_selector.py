from flask import Blueprint, render_template

continent_selector_bp = Blueprint(
    "continent_selector",
    __name__,
    template_folder="templates"
)

@continent_selector_bp.route("/country-from-flag/continent-selector", methods=["GET", "POST"])
def continent_selector():
    return render_template(
        template_name_or_list="flag_to_country/continent_selector.html"
    )
