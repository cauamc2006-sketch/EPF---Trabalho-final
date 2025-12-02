% title = jogo.nome

<div class="detalhes-container">
    <div class="imagem-detalhe">
        <img src="{{ jogo.imagem }}" alt="{{ jogo.nome }}">
    </div>

    <div class="info-detalhe">
        <h1>{{ jogo.nome }}</h1>
        
        <p class="genero">Categoria: **{{ jogo.descricao }}**</p>
        
        <div class="descricao">
            <h2>Sobre o Jogo:</h2>
            <p>...</p>
        </div>

        <div class="preco-compra">
            <span class="preco-final">R$ {{ "%.2f" % jogo.preco }}</span>
            <button class="btn-comprar">Adicionar ao Carrinho</button>
        </div>

        <a href="/" class="btn-voltar">← Voltar para a Home</a>
    </div>
</div>