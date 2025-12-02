% rebase('base.tpl', title=title)

<h1>Categoria: {{categoria}}</h1>

<div class="jogos-lista">
% for jogo in jogos:
    <div class="jogo-card">
        <a href="/games/{{jogo['get_id()']}}">
            <img src="{{jogo['get_imagem()']}}" alt="{{jogo['get_nome()']}}">
            <h3>{{jogo['get_nome()']}}</h3>
            <p>R$ {{jogo['get_preco()']}}</p>
        </a>
    </div>
% end
</div>

<a href="/categorias">⬅ Voltar</a>