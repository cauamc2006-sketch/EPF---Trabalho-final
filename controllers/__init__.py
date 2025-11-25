from bottle import Bottle
from controllers.user_controller import user_routes
from controllers.pags_controller import pags_routes


def init_controllers(app: Bottle):
    app.merge(user_routes)
    app.merge(pags_routes)