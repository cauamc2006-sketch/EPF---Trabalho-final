% rebase('layout.tpl')
% title = jogo.get_nome()

<div class="pagina-jogo">

    <img src="{{ jogo.get_imagem() }}" class="img-jogo">

    <h1>{{ jogo.get_nome() }}</h1>

    <p>Gênero: {{ jogo.get_genero() }}</p>

    <p>Preço: R$ {{ "%.2f" % jogo.get_preco() }}</p>

    <a href="/jogos">Voltar</a>

</div>