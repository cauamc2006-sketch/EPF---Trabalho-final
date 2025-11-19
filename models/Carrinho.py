from Jogo import Jogo

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
        

  
        
#j1 = Jogo(3, "Fortnite", 200, "Battle royale")
#j2 = Jogo(2,"Resident Evil", 200 , "terror")

#c1 = Carrinho()

#c1.adicionar_jogo(j1)
#c1.adicionar_jogo(j2)
#c1.exibir_lista()

#c1.calcular_total()
       
       
    