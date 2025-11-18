class Jogo:
   
    def __init__(self, id, nome, preco, genero):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.genero = genero
    
    
    def atualizar_preco(self,novo_preco: float):
        if (novo_preco == self.preco):
            print("Digite um preço diferente do atual!!!")
        else:
            self.preco = novo_preco
            print(f"Preço atualizado com sucesso!!!, seu preço agora é R${novo_preco}")  


j1 = Jogo(2,"Resident-Eviel", 200 , "terror")

print(j1.preco)
    

    