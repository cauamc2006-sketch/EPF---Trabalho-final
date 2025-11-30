from controllers.home_controller import home_routes
from controllers.user_controller import user_routes
from controllers.jogo_controller import jogo_routes
from controllers.carrinho_controller import carrinho_routes
from controllers.categoria_controller import categoria_routes

def init_controllers(app):
    app.merge(home_routes)
    app.merge(user_routes)
    app.merge(jogo_routes)
    app.merge(carrinho_routes)
    app.merge(categoria_routes)

