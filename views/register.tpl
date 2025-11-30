

<h2>Cadastro</h2>

% if error:
    <div class="alert alert-danger">{{error}}</div>
% end

<form method="POST" action="/register" class="form">
    <label for="username">Usuário:</label>
    <input type="text" name="username" required>

    <label for="email">E-mail:</label>
    <input type="email" name="email">

    <label for="password">Senha:</label>
    <input type="password" name="password" required>

    <button type="submit">Registrar</button>
</form>

<p>Já tem conta? <a href="/login">Entrar</a></p>
