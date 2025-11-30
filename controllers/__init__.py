
from controllers.user_controller import user_routes
from controllers.jogo_controller import jogo_routes

def init_controllers(app):
    
    app.merge(user_routes)
    app.merge(jogo_routes)
