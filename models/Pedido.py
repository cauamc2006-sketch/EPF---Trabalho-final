from Jogo import Jogo
from Carrinho import Carrinho
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
        
c1 = Carrinho()
c2 = Carrinho()
            
j3 = Jogo(2,"Resident Evil", 200 , "terror")
j2 = Jogo(3, "Fifa 26", 350, "esporte" )
j4 = Jogo(4, "Mortal Kombat", 80 , "Luta")
c1.adicionar_jogo(j3)
c1.adicionar_jogo(j2)
c2.adicionar_jogo(j4)
p1 = Pedido(1, c1)
p2 = Pedido(2, c2)
p1.exibir_pedido()
p2.exibir_pedido()
j4.atualizar_preco(50)
p2.exibir_pedido


