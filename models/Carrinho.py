from jogo import Jogo

class Carrinho:
    
    def __init__(self):
        self.__itens = []
        
    def get_itens(self):
        return self.__itens
    
    def get_total(self):
        return sum(item.get_preco() for item in self.__itens)
    
    def adicionar_jogo(self, jogo: Jogo):
        self.get_itens().append(jogo)
        print(f"Jogo {jogo.get_nome()} adicionado no seu carrinho!")
        
    
    def exibir_lista(self):
        for jogo in self.itens:
            print(jogo.get_nome())
        print("--------")
     
        
    def remover_jogo(self, jogo: Jogo):
        self.__itens.remove(jogo)
        print(f"Jogo {jogo.get_nome()} removido do seu carrinho!")
        

  
        

       
       
    