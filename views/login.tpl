% title = "login"



<h2>Login</h2>

% if error:
    <div class="alert alert-danger">{{error}}</div>
% end

<form method="POST" action="/login" class="form">
    <label for="username">Usuário:</label>
    <input type="text" name="username" required>

    <label for="password">Senha:</label>
    <input type="password" name="password" required>

    <button type="submit">Entrar</button>
</form>

<p>Não tem conta? <a href="/register">Cadastrar</a></p>
