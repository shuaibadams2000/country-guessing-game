from flask import Flask
from flask_bootstrap import Bootstrap

# Route imports
from routes.flag_to_country.flag_to_country_route import country_from_flag_bp
from routes.flag_to_country.continent_selector import continent_selector_bp
from routes.home_route import home_bp


def create_app():
    app = Flask(__name__)
    app.secret_key = "secret_key"
    Bootstrap(app)
    app.register_blueprint(home_bp)
    app.register_blueprint(country_from_flag_bp)
    app.register_blueprint(continent_selector_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5001)
