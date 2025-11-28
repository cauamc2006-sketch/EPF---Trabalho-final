from models.Jogo import JogoModel, Jogo


class JogoService:
    def __init__(self):
        self.model = JogoModel()

    
    def listar_jogos(self):
        return self.model.get_all()

    def buscar_por_id(self, jogo_id: int):
        jogo = self.model.get_by_id(jogo_id)
        if not jogo:
            raise ValueError("Jogo não encontrado!")
        return jogo

  

    def adicionar_jogo(self, id, nome, preco, genero):
        if self.model.get_by_id(id):
            raise ValueError("Já existe um jogo com esse ID")

        jogo = Jogo(id=id, nome=nome, preco=preco, genero=genero)
        self.model.add_jogo(jogo)
        return jogo

    def atualizar_preco(self, jogo_id, novo_preco):
        jogo = self.buscar_por_id(jogo_id)
        jogo.atualizar_preco(novo_preco)
        self.model.update_jogo(jogo)
        return jogo

    def remover_jogo(self, jogo_id):
        if not self.model.get_by_id(jogo_id):
            raise ValueError("Não existe jogo com esse ID")

        self.model.delete_jogo(jogo_id)
        return True
