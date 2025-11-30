from models.jogo import JogoModel, Jogo


class JogoService:
    def __init__(self):
        self.model = JogoModel()

    def listar_jogos(self):
        return self.model.get_all()

    def get_by_id(self, jogo_id):
        return self.model.get_by_id(jogo_id)

    def adicionar_jogo(self, nome, preco, genero, imagem):
        jogos = self.model.get_all()
        new_id = (jogos[-1].get_id() + 1) if jogos else 1

        novo = Jogo(new_id, nome, preco, genero, imagem)
        self.model.add_jogo(novo)

    def remover_jogo(self, jogo_id):
        self.model.delete_jogo(jogo_id)