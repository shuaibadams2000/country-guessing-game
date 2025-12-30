from flask import Flask
from flask_bootstrap import Bootstrap

# Route imports
from routes.flag_to_country_route import country_from_flag_bp
from routes.home_route import home_bp


def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.register_blueprint(home_bp)
    app.register_blueprint(country_from_flag_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5001)
