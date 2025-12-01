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
        self.app.get("/carrinho", callback=self.index)
        self.app.get("/carrinho/add/<jogo_id:int>", callback=self.add)
        self.app.get("/carrinho/remove/<jogo_id:int>", callback=self.remove)
        self.app.get("/carrinho/clear", callback=self.clear)
        self.app.post("/carrinho/finalizar", callback=self.finalizar)



    def index(self):
        user = self._get_user()
        if not user:
            return self.redirect("/login")

        jogos = self.carrinho_service.get_carrinho_completo(user)

        total = sum(j.get_preco() for j in jogos)

        print("DEBUG TOTAL =", total)  # <-- teste


        return self.render("carrinho", jogos=jogos, total=total)

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

    def finalizar(self):
        user = self._get_user()
        if not user:
            return self.redirect("/login")

        total = self.carrinho_service.finalizar_compra(user)

        return self.render("compra_finalizada", total=total)


carrinho_routes = Bottle()
CarrinhoController(carrinho_routes)
