% title = get('title', 'Sistema')

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jogos St0re - {{title or 'Sistema'}}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="shortcut icon" href="/static/img/controle-16.ico" type="image/x-icon">
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>

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
