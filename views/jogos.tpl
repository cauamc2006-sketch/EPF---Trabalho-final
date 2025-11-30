<h1>Lista de Jogos</h1>

<ul>
% for jogo in jogos:
    <li>{{ jogo.get_nome() }} - R$ {{ jogo.get_preco() }}</li>
% end
</ul>
