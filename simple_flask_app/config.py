"""Config settings for for development, testing and production environments."""
import os


class BaseConfig:
    """Base configuration."""

    # APP SETTINGS
    APP_NAME = os.environ.get('APP_NAME', 'Simple Flask App')
    APP_WEB_URL = os.environ.get('APP_WEB_URL', 'http://localhost:5000')
    API_VERSION = os.environ.get('API_VERSION', '0.0.1')
    API_CONTEXT = os.environ.get('API_CONTEXT', 'develop')
    FLASK_ENV = os.environ.get('FLASK_ENV', 'development')

    # LOG SETTINGS
    LOG_BACKTRACE = True
    LOGFILE = os.environ.get('APP_LOG', 'logs/app.log')
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG')

    # NASA API SETTINGS
    NASA_API_KEY = os.environ.get('NASA_API_KEY', 'DEMO_KEY')


class TestingConfig(BaseConfig):
    """Testing configuration."""

    CONTEXT = 'test'


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    CONTEXT = 'develop'


class ProductionConfig(BaseConfig):
    """Production configuration."""

    CONTEXT = 'production'


ENV_CONFIG_DICT = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig
)


def get_config(config_name):
    """Retrieve environment configuration settings."""

    return ENV_CONFIG_DICT.get(config_name, ProductionConfig)
