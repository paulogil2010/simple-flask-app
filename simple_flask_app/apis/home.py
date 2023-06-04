import os
import logging
import requests
from flask import Blueprint, render_template
from faker import Faker

from simple_flask_app.config import get_config


CONFIG = get_config(os.getenv("FLASK_ENV", "development"))
LOGGER = logging.getLogger(__name__)

home_blueprint = Blueprint('home', __name__)


@home_blueprint.route('/')
def home():
    base_url = 'https://api.nasa.gov/planetary/apod'
    api_key = CONFIG.NASA_API_KEY
    fake = Faker()
    fake_date = str(fake.date_between(start_date='-1y', end_date='today'))
    LOGGER.info('Calling NASA API with date: %s', fake_date)

    response = requests.get(
        base_url,
        params={
            'api_key': api_key,
            'date': fake_date
        }
    )
    data = response.json()
    image_url = data['url']
    image_description = data['explanation']

    image_url = data['url']
    image_description = data['explanation']
    return render_template(
        'home.html',
        image_url=image_url,
        image_description=image_description,
        fake_date=fake_date
    )
