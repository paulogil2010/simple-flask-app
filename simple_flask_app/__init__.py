import os
import logging
from flask import Flask

from simple_flask_app.apis.home import home_blueprint
from simple_flask_app.config import get_config


LOGGER = logging.getLogger(__name__)
LOGGER.level = logging.INFO
CONFIG = get_config(os.getenv("FLASK_ENV", "development"))


def flask():
    app = Flask(__name__)
    app.config.from_object(CONFIG)
    app.logger.setLevel(CONFIG.LOG_LEVEL)
    LOGGER.info('Configuring Flask')
    return app


def register_blueprints(app):
    app.register_blueprint(home_blueprint)
    LOGGER.info('Registering blueprints')


def create_app():
    """Create a Flask application using the app factory pattern.

    Returns:
        Flask: A Flask application.
    """

    app = flask()
    register_blueprints(app)
    return app
