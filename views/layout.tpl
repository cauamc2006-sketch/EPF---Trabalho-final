% title = get('title', 'Sistema')

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jogos St0re - {{title or 'Sistema'}}</title>
    <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="shortcut icon" href="/static/img/controle-16.ico" type="image/x-icon">
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>

<header class="header">
    <div class="header-cn">
                <img src="/static/img/ICON_SITE-def.png"alt="Logo"class=logo>
 
                <nav class="nav-menu">
                    <a href="/">INÍCIO</a>
                </nav>
        <a href="/carrinho" class="carrinho-aba">CARRINHO</a>   
                 
        <a href="/categorias" class="categorias">CATEGORIAS</a>
        <a href="/login" class="btn-login">LOGIN</a>
        <a href="/register" class = "registro">REGISTRAR</a>
        
        <input type="text" class="barra-pesquisa" placeholder="🔍PESQUISAR...">
    </div>
</header>
 <div class="container">
        {{!base}}  <!-- O conteúdo das páginas filhas virá aqui -->
    </div>

    <footer>
        <p>&copy; 2025, Meu Projeto. Todos os direitos reservados.</p>
    </footer>

    <!-- Scripts JS no final do body -->
    <script src="/static/js/main.js"></script>
</body>
</html>
