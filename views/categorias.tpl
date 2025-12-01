<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Categorias</title>
    <style>
        body { font-family: Arial; }
        ul { list-style: none; padding: 0; }
        li { 
            background: #f2f2f2;
            margin: 4px 0;
            padding: 10px;
            border-radius: 6px;
        }
    </style>
</head>
<body>
    <h1>Lista de Categorias</h1>

   % for cat in categorias:
    <li>
        <a href="/categorias/{{cat}}">{{cat}}</a>
    </li>
    % end


    <br>
    <a href="/">Voltar</a>
</body>
</html>
