from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from config import config


bootstrap = Bootstrap()
mail = Mail()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)

    # attach routes and custom error pages here

    return app