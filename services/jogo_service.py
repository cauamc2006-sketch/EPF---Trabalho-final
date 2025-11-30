from models.jogo import Jogo
from models.jogo import JogoModel

class JogoService:
    def __init__(self):
        self.model = JogoModel()

    def listar_jogos(self):
        return self.model.get_all()

    def get_by_id(self, jogo_id):
        return self.model.get_by_id(jogo_id)

    def adicionar_jogo(self, nome, preco, genero, imagem):
        jogos = self.model.get_all()
        new_id = jogos[-1]["id"] + 1 if jogos else 1

        novo = Jogo(new_id, nome, preco, genero, imagem)
        self.model.add_jogo(novo)

    def remover_jogo(self, jogo_id):
        self.model.delete(jogo_id)

    def get_categorias(self):
        jogos = self.model.get_all()
        categorias = list(set(j.categoria for j in jogos))
        return categorias

    def get_by_categoria(self, categoria):
        jogos = self.model.get_all()
        cat_lower = (categoria or "").lower()
        return [
        j for j in jogos
        if getattr(j, "categoria", None) and isinstance(j.categoria, str)
           and j.categoria.lower() == cat_lower
    ]


