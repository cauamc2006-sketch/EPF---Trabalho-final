import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')


class Jogo:
    def __init__(self, id, nome, preco, genero, imagem=None):
        self.__id = id
        self.__nome = nome
        self.__preco = preco
        self.__genero = genero
        self.__imagem = imagem  # opcional

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def get_genero(self):
        return self.__genero

    def get_imagem(self):
        return self.__imagem

    def to_dict(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "preco": self.__preco,
            "genero": self.__genero,
            "imagem": self.__imagem
        }


class JogoModel:
    FILE_PATH = os.path.join(DATA_DIR, 'jogos.json')

    def __init__(self):
        self.jogos = self._load()

    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Jogo(**item) for item in data]

    def _save(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([j.to_dict() for j in self.jogos], f, indent=4, ensure_ascii=False)

    def get_all(self):
        return self.jogos

    def get_by_id(self, jogo_id):
        return next((j for j in self.jogos if j.get_id() == jogo_id), None)

    def add_jogo(self, jogo):
        self.jogos.append(jogo)
        self._save()

    def delete_jogo(self, jogo_id):
        self.jogos = [j for j in self.jogos if j.get_id() != jogo_id]
        self._save()