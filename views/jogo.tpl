% rebase('layout.tpl')
% title = jogo.get_nome()

<div class="pagina-jogo">

    <div class="jogo-container">

        <img src="{{ jogo.get_imagem() }}" class="img-jogo">

        <div class="info-jogo">
            <h1>{{ jogo.get_nome() }}</h1>

            <p class="genero">Gênero: <span>{{ jogo.get_genero() }}</span></p>

            <p class="preco">
                R$ {{ "%.2f" % jogo.get_preco() }}
            </p>

            <a href="/jogos" class="btn-voltar">Voltar</a>
        </div>

    </div>

</div>