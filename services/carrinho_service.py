from models.Carrinho import CarrinhoModel
from models.jogo import JogoModel

class CarrinhoService:
    def __init__(self):
        self.carrinho_model = CarrinhoModel()
        self.jogo_model = JogoModel()

    def get_carrinho_completo(self, user_id):
        ids = self.carrinho_model.get_carrinho(user_id)
        return [self.jogo_model.get_by_id(j) for j in ids if self.jogo_model.get_by_id(j)]

    def add(self, user_id, jogo_id):
        self.carrinho_model.add_item(user_id, jogo_id)

    def remove(self, user_id, jogo_id):
        self.carrinho_model.remove_item(user_id, jogo_id)

    def clear(self, user_id):
        self.carrinho_model.clear(user_id)

    def finalizar_compra(self, user_id):
        jogos = self.get_carrinho_completo(user_id)

        total = sum(j.get_preco() for j in jogos)

        self.clear(user_id)

        return total
