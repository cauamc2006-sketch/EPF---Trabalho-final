import json
import os
from dataclasses import dataclass, asdict
from typing import List
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class Jogo:
   
    def __init__(self, id, nome, preco, genero):
        self.__id = id
        self.__nome = nome
        self.__preco = preco
        self.__genero = genero
        
    def get_id(self):
        return self.__id
    
    def get_preco(self):
        return self.__preco
    
    def get_nome(self):
        return self.__nome
    
    def get_genero(self):
        return self.__genero
    
    
    def atualizar_preco(self,novo_preco: float):
        if (novo_preco == self.get_preco()):
            print("Digite um preço diferente do atual!")
        else:
            self.__preco = novo_preco
            print(f"Preço atualizado com sucesso!, preço de {self.__nome} agora é R${novo_preco:.2f}")  
            
    

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
            json.dump([u.to_dict() for u in self.jogos], f, indent=4, ensure_ascii=False)


    def get_all(self):
        return self.jogos


    def get_by_id(self, jogo_id: int):
        return next((u for u in self.jogos if u.id == jogo_id), None)


    def add_jogo(self, jogo: Jogo):
        self.jogos.append(jogo)
        self._save()


    def update_jogo(self, updated_jogo: Jogo):
        for i, jogo in enumerate(self.jogos):
            if jogo.id == updated_jogo.id:
                self.jogos[i] = updated_jogo
                self._save()
                break


    def delete_jogo(self, jogo_id: int):
        self.jogos = [u for u in self.jogos if u.id != jogo_id]
        self._save()




    