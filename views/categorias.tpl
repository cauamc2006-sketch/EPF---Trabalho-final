% rebase('layout.tpl')
% title = "Categorias"

<div class="categorias-container">
    <h2>{{ title }}</h2>

    <ul class="categorias-list">
    % # 1. Garante que é um dicionário e itera sobre chave/valor
    % if isinstance(categorias, dict):
        % for categoria_nome, jogo in categorias.items():
            <li class="categoria-item">
                <a href="/jogos?genero={{ categoria_nome }}">
                    
                    <img src="{{ jogo.get_imagem() }}" alt="Jogo da Categoria {{ categoria_nome }}" class="categoria-image">
                    
                    <span class="categoria-title">{{ categoria_nome }}</span>
                </a>
            </li>
        % end
    % else:
        <li>Erro: O formato das categorias está incorreto.</li>
    % end
    </ul>
</div>