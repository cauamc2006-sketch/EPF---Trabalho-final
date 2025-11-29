from bottle import Bottle, request
from .base_controller import BaseController
from services.user_service import UserService

class UserController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.auth_service = UserService()
        self.setup_routes()

    # ROTAS
    def setup_routes(self):
        self.app.route('/login',   method=['GET', 'POST'], callback=self.login)
        self.app.route('/logout',  method='GET', callback=self.logout)
        self.app.route('/register', method=['GET', 'POST'], callback=self.register)

    # LOGIN
    def login(self):
        if request.method == 'GET':
            return self.render('login', error=None)

        # POST
        username = request.forms.get('username')
        password = request.forms.get('password')

        user = self.auth_service.authenticate(username, password)

        if not user:
            return self.render('login', error="Usuário ou senha incorretos")

        # cria sessão
        self.auth_service.login(user)

        return self.redirect('/')

    # REGISTRO
    def register(self):
        if request.method == 'GET':
            return self.render('register', error=None)

        username = request.forms.get('username')
        password = request.forms.get('password')

        # tenta registrar
        result = self.auth_service.register(username, password)

        if not result:
            return self.render('register', error="Usuário já existe")

        return self.redirect('/login')

    # LOGOUT
    def logout(self):
        self.auth_service.logout()
        return self.redirect('/login')

user_routes = Bottle()
UserController(user_routes)
