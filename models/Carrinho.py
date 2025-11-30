from jogo import Jogo
import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
FILE_PATH = os.path.join(DATA_DIR, 'carrinhos.json')

class CarrinhoModel:
    def __init__(self):
        self.carrinhos = self._load()

    def _load(self):
        if not os.path.exists(FILE_PATH):
            return {}
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)

    def _save(self):
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(self.carrinhos, f, indent=4, ensure_ascii=False)

    def get_carrinho(self, user_id):
        return self.carrinhos.get(str(user_id), [])

    def add_item(self, user_id, jogo_id):
        user_id = str(user_id)

        if user_id not in self.carrinhos:
            self.carrinhos[user_id] = []

        self.carrinhos[user_id].append(jogo_id)
        self._save()

    def remove_item(self, user_id, jogo_id):
        user_id = str(user_id)

        if user_id in self.carrinhos:
            if jogo_id in self.carrinhos[user_id]:
                self.carrinhos[user_id].remove(jogo_id)
                self._save()

    def clear(self, user_id):
        user_id = str(user_id)
        if user_id in self.carrinhos:
            self.carrinhos[user_id] = []
            self._save()
