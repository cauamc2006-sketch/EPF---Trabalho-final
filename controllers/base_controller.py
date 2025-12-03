from bottle import static_file, request, response # <<< CORRIGIDO: Adiciona response e request
from models.jogo import JogoModel
from bottle import redirect as bottle_redirect


class BaseController:
    def __init__(self, app):
        self.app = app
        self._setup_base_routes()


    def _setup_base_routes(self):
        """Configura rotas básicas comuns a todos os controllers"""
        self.app.route('/', method='GET', callback=self.home_redirect)
        self.app.route('/helper', method=['GET'], callback=self.helper)
        self.app.route('/categorias', method='GET', callback=self.categorias_page) # Rota de categorias

        # Rota para arquivos estáticos (CSS, JS, imagens)
        self.app.route('/static/<filename:path>', callback=self.serve_static)

    # NOVO MÉTODO: Verifica se o usuário está logado
    def pegar_id_usuario_logado(self):
        """Lê o cookie de sessão para obter o ID do usuário."""
        usuario_id = request.get_cookie("user_id")
        return usuario_id if usuario_id else None

    def home_redirect(self):
        model = JogoModel()
        todos_jogos = model.get_all()
        termo_busca = request.query.get('termo', '').strip().lower()
        
        jogos_filtrados = []
        msg_busca = None
        
        # Lista a ser exibida (começa assumindo que será a lista completa)
        jogos_para_exibir = todos_jogos 

        if termo_busca:
            # 1. Executa a Filtragem
            for jogo in todos_jogos:
                try:
                    nome_jogo = jogo.get_nome().lower()
                    genero_jogo = jogo.get_genero().lower()
                except AttributeError:
                    continue

                if termo_busca in nome_jogo or termo_busca in genero_jogo:
                    jogos_filtrados.append(jogo)

            # 2. LÓGICA DE TRATAMENTO DE RESULTADOS
            if len(jogos_filtrados) == 1:
                # Caso 1: Sucesso e Jogo Único -> Redireciona
                jogo_unico = jogos_filtrados[0]
                return self.redirect(f"/jogo/{jogo_unico.get_id()}")
                
            elif len(jogos_filtrados) > 0:
                # Caso 2: Sucesso e Múltiplos Jogos -> Exibe o resultado filtrado
                jogos_para_exibir = jogos_filtrados
                
            else:
                # Caso 3: NENHUM JOGO ENCONTRADO.
                jogos_para_exibir = todos_jogos
                # Define a mensagem de erro para ser exibida no template
                msg_busca = f"Busca por '{termo_busca}' não encontrou resultados. Exibindo todos os jogos."
                
        # O método render injetará a variável de login e a mensagem de busca
        return self.render('home', title='Home', jogos=jogos_para_exibir, mensagem_busca=msg_busca)


    def helper(self):
        return self.render('helper-final')


    def serve_static(self, filename):
        """Serve arquivos estáticos da pasta static/"""
        return static_file(filename, root='./static')


    # MÉTODO RENDER CORRIGIDO: Injeta o status de login em TODAS as renderizações
    def render(self, template, **context):
        """Método auxiliar para renderizar templates, injetando o status de login"""
        
        # INJETA A VARIÁVEL DE LOGIN (Resolve o NameError no layout.tpl)
        context['usuario_logado_id'] = self.pegar_id_usuario_logado()
        
        from bottle import template as render_template
        return render_template(template, **context)

    # Método redirect e categorias_page, movidos e limpos
    def redirect(self, path, code=302):
        """Redireciona usando o redirect nativo do Bottle"""
        # A parte com 'try' e 'HTTPResponse' não é padrão e foi removida para simplificar.
        return bottle_redirect(path, code=code)

    def categorias_page(self):
        """Página que lista todas as categorias disponíveis"""
        model = JogoModel()
        # Assume que get_categorias() está implementado no JogoModel
        categorias = model.get_categorias() 

        return self.render('categorias', categorias=categorias)