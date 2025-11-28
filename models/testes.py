from Carrinho import Carrinho
from Jogo import Jogo 
from Pedido import Pedido

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
