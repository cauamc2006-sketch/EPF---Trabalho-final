% rebase('layout', title='Formulário Usuário')

<section class="form-sections">
    <h1>{{'Editar Usuário' if user else 'Adicionar Usuário'}}</h1>
    
    <form action="{{action}}" method="post" class="form-container">
           
            <div class="form-group">
                <label for="name">Nome:</label>
                <input type="text" id="name" name="name" class="nome-barra" required 
                    value="{{user.name if user else ''}}" placeholder="Digite seu nome...">
            </div>
            
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" class="email-barra" required 
                    value="{{user.email if user else ''}}" placeholder="Digite seu email...">
            </div>
            
            <div class="form-group">
                <label for="birthdate">Data de Nascimento:</label>
                <input type="date" id="birthdate" name="birthdate" class="id-barra" required 
                    value="{{user.birthdate if user else ''}}">
            </div>
            
            <div class="form-actions">
                <button type="submit" class="btn-submit">Salvar</button>
                <a href="/users" class="btn-cancel">Voltar</a>
            </div>
            
    </form>
</section>