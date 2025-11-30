from bottle import Bottle, request
from .base_controller import BaseController
from services.carrinho_service import CarrinhoService
from services.user_service import UserService


class CarrinhoController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.carrinho_service = CarrinhoService()
        self.user_service = UserService()
        self.setup_routes()

    def _get_user(self):
        return request.get_cookie("user_id")

    def setup_routes(self):
        self.app.route("/carrinho", "GET", self.index)
        self.app.route("/carrinho/add/<jogo_id:int>", "GET", self.add)
        self.app.route("/carrinho/remove/<jogo_id:int>", "GET", self.remove)
        self.app.route("/carrinho/clear", "GET", self.clear)

    def index(self):
        user = self._get_user()
        if not user:
            return self.redirect("/login")

        jogos = self.carrinho_service.get_carrinho_completo(user)

        return self.render("carrinho", jogos=jogos)

    def add(self, jogo_id):
        user = self._get_user()
        if not user:
            return self.redirect("/login")

        self.carrinho_service.add(user, jogo_id)
        return self.redirect("/carrinho")

    def remove(self, jogo_id):
        user = self._get_user()
        if not user:
            return self.redirect("/login")

        self.carrinho_service.remove(user, jogo_id)
        return self.redirect("/carrinho")

    def clear(self):
        user = self._get_user()
        if not user:
            return self.redirect("/login")

        self.carrinho_service.clear(user)
        return self.redirect("/carrinho")


carrinho_routes = Bottle()
CarrinhoController(carrinho_routes)
