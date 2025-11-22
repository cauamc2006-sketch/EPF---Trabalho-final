class Jogo:
   
    def __init__(self, id, nome, preco, genero):
        self.__id = id
        self.__nome = nome
        self.__preco = preco
        self.__genero = genero
    
    def get_preco(self):
        return self.__preco
    
    def get_nome(self):
        return self.__nome
    
    
    def atualizar_preco(self,novo_preco: float):
        if (novo_preco == self.get_preco()):
            print("Digite um preço diferente do atual!")
        else:
            self.preco = novo_preco
            print(f"Preço atualizado com sucesso!, seu preço agora é R${novo_preco:.2f}")  


j3 = Jogo(2,"Resident-Eviel", 200 , "terror")

#j3.atualizar_preco(350)
#print(j1.preco)



    