<h1>Lista de Jogos</h1>

<ul>
% for jogo in jogos:
    <li>{{ jogo.nome }} - R$ {{ jogo.preco }}</li>
% end
</ul>
