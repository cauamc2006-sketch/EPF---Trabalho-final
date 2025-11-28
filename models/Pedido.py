import json
import os
from dataclasses import dataclass, asdict
from typing import List
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class Pedido:
    
    def __init__(self,id_pedido, carrinho):
        self.__id_pedido = id_pedido
        self.__itens = carrinho.get_itens()
        self.__total = carrinho.get_total()
        print("Pedido criado com sucesso!")
        
    def get_idPedido(self):
        return self.__id_pedido
    
    def exibir_pedido(self):
        print(f"ID do pedido: {self.__id_pedido}")
        print("\nItens do pedido:")
        for item in self.__itens:
            print(f"- {item.get_nome()} | R$ {item.get_preco():.2f}")
        print("- - - - - - - - - - -")    
        print(f"\nTotal: R$ {self.__total:.2f}")
        
        
        
    def to_dict(self):
        return{
            'id': self.__id_pedido,
            'Itens': self.__itens,
            'Total': self.__total
        }

class PedidoModel:
    FILE_PATH = os.path.join(DATA_DIR, 'pedidos.json')

    def __init__(self):
        self.pedidos = self._load()


    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Pedido(**item) for item in data]


    def _save(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([u.to_dict() for u in self.pedidos], f, indent=4, ensure_ascii=False)


    def get_all(self):
        return self.pedidos


    def get_by_id(self, user_id: int):
        return next((u for u in self.pedidos if u.id == user_id), None)


    def add_user(self, user: Pedido):
        self.pedidos.append(user)
        self._save()


    def update_user(self, updated_user: Pedido):
        for i, user in enumerate(self.pedidos):
            if user.id == updated_user.id:
                self.pedidos[i] = updated_user
                self._save()
                break


    def delete_user(self, user_id: int):
        self.pedidos = [u for u in self.pedidos if u.id != user_id]
        self._save()  



