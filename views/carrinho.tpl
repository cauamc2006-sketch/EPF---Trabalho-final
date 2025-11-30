% rebase('layout.tpl')
% title = "Seu Carrinho"

<h1>Seu Carrinho</h1>

% if not jogos:
    <p>Seu carrinho está vazio.</p>
% else:
    % for jogo in jogos:
        <div class="item-carrinho">
            <img src="{{ jogo.get_imagem() }}" width="100">
            <strong>{{ jogo.get_nome() }}</strong>
            <span>R$ {{ "%.2f" % jogo.get_preco() }}</span>
            <a href="/carrinho/remove/{{ jogo.get_id() }}">Remover</a>
        </div>
    % end

    <a href="/carrinho/clear">Esvaziar carrinho</a>
% end
