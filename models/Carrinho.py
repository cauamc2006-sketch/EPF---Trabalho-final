from Jogo import Jogo

class Carrinho:
    
    def __init__(self):
        self.itens = []
        
        
    def adicionar_jogo(self, jogo: Jogo):
        self.itens.append(jogo)
        print(f"Jogo {jogo.nome} adicionado na sua lista!!")
        
    
    def exibir_lista(self):
        for jogo in self.itens:
            print(jogo.nome)
        print("--------")
     
        
    def remover_jogo(self, jogo: Jogo):
        self.itens.remove(jogo)
        print(f"Jogo {jogo.nome} removido de sua lista!")
        

    def calcular_total(self):
        total = 0
        for jogo in self.itens:
            total += jogo.preco
            
        print(f"Total: R${total:.2f}")
        
j1 = Jogo(3, "Fortnite", 200, "Battle royale")
j2 = Jogo(2,"Resident Evil", 200 , "terror")

c1 = Carrinho()

c1.adicionar_jogo(j1)
c1.adicionar_jogo(j2)
c1.exibir_lista()

c1.calcular_total()
       
       
    