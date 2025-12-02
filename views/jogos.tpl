% rebase('layout.tpl')
 <style>
       

        .explorar-container {
            padding: 20px;
            max-width: 900px;
            margin: auto;
        }

        .explorar-lista {
            display: flex;
            flex-direction: column; 
            gap: 25px;
        }

        .jogo-card {
            background: #1f2833;
            border-radius: 12px;
            padding: 12px;
            display: flex;
            gap: 18px;
            align-items: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.4);
        }

        .jogo-card img {
            width: 110px;
            height: 150px;
            object-fit: cover;
            border-radius: 10px;
        }

        .info h3 {
            margin: 0;
            font-size: 20px;
            color: #fff;
        }

        .info p {
            margin: 4px 0;
            color: #ccc;
        }

    .jogo-card .preco {
    color: #00ff5a;
    font-weight: bold;
    margin-top: 10px;
}
    </style>
</head>

<body>
<div class="explorar-container">
    <h2>Todos os Jogos</h2>

    <div class="explorar-lista">
        % for jogo in jogos:
        <div class="jogo-card">
            <a href="/jogo/{{ jogo.get_id() }}">
                <img src="{{ jogo.get_imagem() }}" alt="{{ jogo.get_nome() }}">
            </a>

            <div class="info">
                <h3>{{ jogo.get_nome() }}</h3>
                <p>{{ jogo.get_genero() }}</p>
                <p class="preco">R$ {{ "%.2f" % jogo.get_preco() }}</p>
            </div>
        </div>
        % end
    </div>
</div>


