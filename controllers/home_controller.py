from bottle import Bottle
from controllers.base_controller import BaseController
from models.jogo import JogoModel

home_routes = Bottle()

class HomeController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        @app.get('/home')
        def home():
            jogos = JogoModel.load_all()  # Carrega do JSON
            return self.render('home', title='Home', jogos=jogos)