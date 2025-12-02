# Projeto Template: POO com Python + Bottle + JSON

# Lojinha de Jogos

Uma loja virtual simples de jogos construída em Python usando o micro-framework Bottle, com persistência via JSON — projeto para disciplina da universidade, com o prof. Lucas Boaventura.

# Criadores

- Ítalo Carlos Santana Dias do Nascimento- 242015639
- Cauã Mendes Coelho- 242032237

## ✅ Funcionalidades

- Cadastro de usuários e login.  
- Listagem de jogos (a partir de `data/jogos.json`). 
- Adicionar jogos novos (a partir de `data/jogos.json`).
- Carrinho de compras: adicionar e remover jogos.  
- Visualização de carrinho com total atualizado.  
- Finalização de compra.  

## 💡 Objetivo

Fornecer uma base simples, extensível e didática para construção de aplicações web orientadas a objetos com aplicações WEB em Python, ideal para trabalhos finais ou exercícios práticos.

---

## 🗂 Estrutura de Pastas

```bash
poo-python-bottle-template/
├── app.py # Ponto de entrada do sistema
├── config.py # Configurações e caminhos do projeto
├── main.py # Inicialização da aplicação
├── requirements.txt # Dependências do projeto
├── README.md # Este arquivo
├── controllers/ # Controladores e rotas
├── models/ # Definição das entidades (ex: User)
├── services/ # Lógica de persistência (JSON)
├── views/ # Arquivos HTML (Bottle Templating)
├── static/ # CSS, JS e imagens
├── data/ # Arquivos JSON de dados
└── .vscode/ # Configurações opcionais do VS Code
```


---

## 📁 Descrição das Pastas

### `controllers/`
Contém as classes responsáveis por lidar com as rotas da aplicação. Exemplos:
- `user_controller.py`: rotas para listagem, adição, edição e remoção de usuários.
- `base_controller.py`: classe base com utilitários comuns.

### `models/`
Define as classes que representam os dados da aplicação. Exemplo:
- `user.py`: classe `User`, com atributos como `id`, `username`, `email`, `password` etc.
- `jogo.py`: classe `jogo`, com atributos como `id`, `nome`, `preco`, `imagem` etc.
- `Carrinho.py`: classe `Carrinho`, ação que manipula o objeto jogo.

### `services/`
Responsável por salvar, carregar e manipular dados usando arquivos JSON. Exemplo:
- `user_service.py`: contém métodos como `get_all`, `register`, `delete`.
- `jogo_service.py`: contém metodos como `listar_jogos`, `get_by_id` etc.
- `carrinho_service.py`: contém metodos como `finalizar_compra`,  etc.

### `views/`
Contém os arquivos `.tpl` utilizados pelo Bottle como páginas HTML:
- `layout.tpl`: estrutura base com navegação e bloco `content`.
- `home.tpl`: pagina principal.
- `carrinho`: formulário para adicionar/remover jogos.

### `static/`
Arquivos estáticos como:
- `css/style.css`: estilos básicos.-
- `img/`: imagens dos jogos.

### `data/`
Armazena os arquivos `.json` que simulam o banco de dados:
- `carrinhos.json`: onde os dados da compra são persistidos.
- `jogos.json`: onde os jogos sao cadastrados e/ou removidos.
- `users.json`: onde os usuarios sao cadastrados e acessados.
---

## ▶️ Como Executar

1. Crie o ambiente virtual na pasta fora do seu projeto:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate     # Windows
```

2. Entre dentro do seu projeto criado a partir do template e instale as dependências:
```bash
pip install -r requirements.txt
```

3. Rode a aplicação:
```bash
python main.py # em caso de erro, tente com "py" ou "python"
```

4. Accese sua aplicação no navegador em: [http://localhost:8080](http://localhost:8080)

---

## ✍️ Personalização
Adicione jogos novos em data/jogos.json seguindo o padrão de atributos dos outros jogos criados!!

---

## 🧠 Autor e Licença
Projeto desenvolvido como template didático para disciplinas de Programação Orientada a Objetos, baseado no [BMVC](https://github.com/hgmachine/bmvc_start_from_this).
