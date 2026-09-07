import bcrypt
from flask import Flask
from .extensions import db, ma, limiter, cache, jwt, bcrypt
from .blueprints.customer import customer_bp
from .blueprints.mechanic import mechanic_bp
from .blueprints.service_ticket import service_ticket_bp
from .blueprints.inventory import inventory_bp


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(f'config.{config_name}')

    db.init_app(app)
    ma.init_app(app)
    limiter.init_app(app)
    bcrypt.init_app(app)
    cache.init_app(app)
    jwt.init_app(app)
    app.register_blueprint(customer_bp, url_prefix='/customers')
    app.register_blueprint(mechanic_bp, url_prefix='/mechanics')
    app.register_blueprint(
        service_ticket_bp,
        url_prefix='/service-tickets'
    )
    app.register_blueprint(
        inventory_bp,
        url_prefix='/inventory'
    )

    return app