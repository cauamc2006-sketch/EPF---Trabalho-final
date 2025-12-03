from bottle import static_file, request, response # <<< CORRIGIDO: Adiciona response e request
from models.jogo import JogoModel
from bottle import redirect as bottle_redirect
from services.user_service import UserService
from models.jogo import Jogo
import os

class BaseController:
    def __init__(self, app):
        self.app = app
        self._setup_base_routes()


    def _setup_base_routes(self):
        """Configura rotas básicas comuns a todos os controllers"""
        self.app.route('/', method='GET', callback=self.home_redirect)
        self.app.route('/helper', method=['GET'], callback=self.helper)
        self.app.route('/categorias', method='GET', callback=self.categorias_page)
        self.app.route('/admin/add-jogo', method=['GET', 'POST'], callback=self.adicionar_jogo_dev) 

        self.app.route('/static/<filename:path>', callback=self.serve_static)

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
                msg_busca = f"Busca por '{termo_busca}' não encontrou resultados. Exibindo todos os jogos."
                
        return self.render('home', title='Home', jogos=jogos_para_exibir, mensagem_busca=msg_busca)


    def helper(self):
        return self.render('helper-final')


    def serve_static(self, filename):
        """Serve arquivos estáticos da pasta static/"""
        return static_file(filename, root='./static')


    def render(self, template, **context):
        """Método auxiliar para renderizar templates, injetando o status de login e request"""
        
        context['usuario_logado_id'] = self.pegar_id_usuario_logado()
        
        context['request'] = request
        
        from bottle import template as render_template
        return render_template(template, **context)

    def redirect(self, path, code=302):
        """Redireciona usando o redirect nativo do Bottle"""
        return bottle_redirect(path, code=code)

    def categorias_page(self):
        """Página que lista todas as categorias disponíveis"""
        model = JogoModel()
        categorias = model.get_categorias() 

        return self.render('categorias', categorias=categorias)
    
    def adicionar_jogo_dev(self):
        user_service = UserService()
        usuario_id = self.pegar_id_usuario_logado()

        if not usuario_id or not user_service.is_admin(int(usuario_id)):
            return self.redirect('/login?error=Acesso restrito a administradores')


        model = JogoModel()
        
        if request.method == 'GET':
            return self.render('admin/add_jogo', error=None)

        nome = request.forms.get('nome')
        preco_str = request.forms.get('preco')
        genero = request.forms.get('genero')
        upload_img = request.files.get('imagem') 
        
        if not all([nome, preco_str, genero, upload_img]):
            return self.render('admin/add_jogo', error="Todos os campos são obrigatórios!")
        
        try:
            preco = float(preco_str.replace(',', '.')) 
        except ValueError:
            return self.render('admin/add_jogo', error="Preço deve ser um número válido.")

        img_filename = None
        if upload_img:
            nome_seguro = upload_img.filename 
            save_path = './static/img'
            
            if not os.path.exists(save_path):
                os.makedirs(save_path)

            final_path = os.path.join(save_path, nome_seguro)
            upload_img.save(final_path, overwrite=True)
            
            img_filename = f"/static/img/{nome_seguro}"
            
        jogos_existentes = model.get_all()
        novo_id = 1
        if jogos_existentes:
            novo_id = max(j.get_id() for j in jogos_existentes) + 1
        
        
        novo_jogo = Jogo(
            id=novo_id,
            nome=nome,
            preco=preco,
            genero=genero,
            imagem=img_filename
        )
        
        model.add_jogo(novo_jogo) 
        
        return self.redirect(f'/jogo/{novo_id}?msg=Jogo adicionado com sucesso!')