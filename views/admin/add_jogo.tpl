% rebase('layout.tpl')
% title = "Adicionar Novo Jogo"

<div class="form-box">
    <h2>Adicionar Novo Jogo (Admin)</h2>

    % if error:
        <div class="alert-danger" 
            {{error}}
        </div>
    % end

    <form method="POST" action="/admin/add-jogo" enctype="multipart/form-data" class="form">
        
        <label for="nome">Nome do Jogo:</label>
        <input type="text" name="nome" value="{{request.forms.get('nome', '')}}" required>

        <label for="preco">Preço (Ex: 199.90):</label>
        <input type="text" name="preco" value="{{request.forms.get('preco', '')}}" required>
        
        <label for="genero">Gênero:</label>
        <input type="text" name="genero" value="{{request.forms.get('genero', '')}}" required>

        <label for="imagem">Imagem do Jogo:</label>
        <input type="file" name="imagem" accept="image/*" required>

        <button type="submit">Adicionar Jogo</button>
    </form>
</div>