% rebase('layout.tpl')
% title = "Home"

    <div class="hero">
        
        <h1>jogos épicos aqui</h1>
        <a class="bnt-hero" href="/jogos">EXPLORAR JOGOS</a> 
    </div>

    <div class="container">
        <div class="tit-principal">
       
            <p><center>OFERTAS RECOMENDADAS:</center></p>
        </div>
            <!--JOGOS-->
       <div class="jogos-grid">

% for jogo in jogos:
    <div class="jogo">
        <a href="/jogo/{{ jogo.get_id() }}">
            <img src="{{ jogo.get_imagem() }}" alt="{{ jogo.get_nome() }}">
            <div class="margem-jogos">
                <h3>{{ jogo.get_nome() }}</h3>
                <p class="categoria">{{ jogo.get_genero() }}</p>
                <p class="preço">R$ {{ "%.2f" % jogo.get_preco() }}</p>
            </div>
        </a>
    </div>
% end
</div>