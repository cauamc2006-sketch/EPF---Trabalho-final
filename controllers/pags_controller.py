from bottle import Bottle
from .base_controller import BaseController

pags_routes = Bottle()

class PagsController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/carrinho', method='GET', callback=self.carrinho)
        self.app.route('/categorias', method='GET', callback=self.categorias)

    def carrinho(self):
        return self.render('carrinho', title="Carrinho")

    def categorias(self):
        return self.render('categorias', title="Categorias")

PagsController(pags_routes)
