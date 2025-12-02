from bottle import static_file, request
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

        # Rota para arquivos estáticos (CSS, JS, imagens)
        self.app.route('/static/<filename:path>', callback=self.serve_static)

    def home_redirect(self):
        model = JogoModel()
        todos_jogos = model.get_all()
        termo_busca = request.query.get('termo', '').strip().lower()
        
        jogos_filtrados = []
        
        jogos_para_exibir = todos_jogos 

        if termo_busca:
            for jogo in todos_jogos:
                try:
                    nome_jogo = jogo.get_nome().lower()
                    genero_jogo = jogo.get_genero().lower()
                except AttributeError:
                    continue

                if termo_busca in nome_jogo or termo_busca in genero_jogo:
                    jogos_filtrados.append(jogo)

            if len(jogos_filtrados) == 1:
                jogo_unico = jogos_filtrados[0]
                return self.redirect(f"/jogo/{jogo_unico.get_id()}")
                
            elif len(jogos_filtrados) > 0:
                jogos_para_exibir = jogos_filtrados
                
            else:
                jogos_para_exibir = todos_jogos
                print(f"Busca por '{termo_busca}' nao encontrou resultados.")
                
        return self.render('home', title='Home', jogos=jogos_para_exibir)

    def helper(self):
        return self.render('helper-final')


    def serve_static(self, filename):
        """Serve arquivos estáticos da pasta static/"""
        return static_file(filename, root='./static')


    def render(self, template, **context):
        """Método auxiliar para renderizar templates"""
        from bottle import template as render_template
        return render_template(template, **context)


    def redirect(self, path, code=302):
        """Redireciona usando o redirect nativo do Bottle, preservando cookies"""
        return bottle_redirect(path, code=code)

        try:
            bottle_response.status = code
            bottle_response.set_header('Location', path)
            return bottle_response
        except Exception as e:
            print(f"ERRO NO REDIRECT: {type(e).__name__} - {str(e)}")
            return HTTPResponse(
                body=f'<script>window.location.href="{path}";</script>',
                status=200,
                headers={'Content-Type': 'text/html'}
            )
    def categorias_page(self):
        """Página que lista todas as categorias disponíveis"""
        model = JogoModel()
        categorias = model.get_categorias()  # <-- Certifique-se de que este método existe no JogoModel

        return self.render('categorias', categorias=categorias)