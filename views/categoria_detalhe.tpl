% rebase('base.tpl', title=title)

<h1>Categoria: {{categoria}}</h1>

<div class="jogos-lista">
% for jogo in jogos:
    <div class="jogo-card">
        <a href="/games/{{jogo['id']}}">
            <img src="{{jogo['imagem']}}" alt="{{jogo['nome']}}">
            <h3>{{jogo['nome']}}</h3>
            <p>R$ {{jogo['preco']}}</p>
        </a>
    </div>
% end
</div>

<a href="/categorias">⬅ Voltar</a>
