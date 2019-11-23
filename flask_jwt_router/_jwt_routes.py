"""
Public class JwtRoutes

The main public API for flask-jwt-router with methods to
handle JSON web tokens.

This pkg creates JwtRouter objects with specific behaviour
based on the cryptographic signing Algorithm.


Quick Start
===========

-----------

Installation::

   pip install flask-jwt-router


Basic Usage::

    from flask import Flask
    from flask_jwt_router import JwtRoutes

    app = Flask(__name__)

    JwtRoutes(app)

    # If you're using the Flask factory pattern:
    jwt_routes = JwtRoutes(entity_model=UserModel)  # Example with *entity_model - see below

    def create_app(config):

        jwt_routes.init_app(app)


Define as a list of tuples::

    app.config["WHITE_LIST_ROUTES"] = [
        ("POST", "/register"),
    ]

    @app.route("/register", methods=["POST"])
    def register():
        return "I don't need authorizing!"


Prefix your api name to whitelisted routes::

    # All routes will
    app.config["JWT_ROUTER_API_NAME"] = "/api/v1"
    app.config["WHITE_LIST_ROUTES"] = [
        ("POST", "/register"),
    ]

    @app.route("/api/v1/register", methods=["POST"])
    def register():
        return "I don't need authorizing!"


Bypass Flask-JWT-Router on specified routes::

    # Define homepage template routes for example on JWT_IGNORE_ROUTES
    # & still get to use the api name on request handlers returning resources
    app.config["IGNORED_ROUTES"] = [
        ("GET", "/")
    ]


Declare an entity model::

    # Create your entity model (example uses Flask-SqlAlchemy)
    class UserModel(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String)
    # You can define the primary key name with `ENTITY_KEY` on Flask's config
    app.config["ENTITY_KEY"] = "user_id"
    # (`id` is used by default)
    JwtRoutes(app, entity_model=UserModel)


Authorization
=============

From your_app import jwt_routes::

    # white list the routes
    app.config["WHITE_LIST_ROUTES"] = [
        ("POST", "/register"),
        ("POST", "/login"),
    ]

    @app.route("/register", methods=["POST"])
    def register():
        # I'm registering a new user & returning a token!
        return jsonify({
            "token": jwt_routes.register_entity(entity_id=1)
        })

    @app.route("/login", methods=["POST"])
    def login():
        # I'm authorized & updating my token!
        return jsonify({
            "token": jwt_routes.update_entity(entity_id=1)
        })

Access entity on Flask's global context::

    # Example uses Marshmallow to serialize entity object
    class EntitySchema(Schema):
        id = fields.Integer()
        name = fields.String()

    @app.route("/user", methods=["GET"])
    def get_user():
        # I was authorized & i have a user!
        entity = EntitySchema().dumps(g.entity).data
        return jsonify({
            "entity": entity
        })

"""
from ._jwt_router import FlaskJWTRouter
from ._authentication import JWTAuthStrategy


class JwtRoutes(FlaskJWTRouter):
    """
    :param: app - Your Flask application instance
    :param: **kwargs - Extension declarations

    """
    def __init__(self, app=None, **kwargs):
        super(JwtRoutes, self).__init__(app, **kwargs)
        self.auth = JWTAuthStrategy()