from bottle import Bottle, request
from .base_controller import BaseController
from services.user_service import UserService

class UserController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.user_service = UserService()
        self.setup_routes()

    
    def setup_routes(self):
        self.app.route('/login',   method=['GET', 'POST'], callback=self.login)
        self.app.route('/logout',  method='GET', callback=self.logout)
        self.app.route('/register', method=['GET', 'POST'], callback=self.register)
        
        
    def login(self):
        if request.method == 'GET':
            return self.render('login', error=None)

        username = request.forms.get('username')
        password = request.forms.get('password')

        user, error = self.user_service.authenticate(username, password)

        if error:
            return self.render('login', error=error)

        return self.redirect('/')


    def register(self):
        if request.method == 'GET':
            return self.render('register', error=None)

        username = request.forms.get('username')
        password = request.forms.get('password')
        email = request.forms.get('email')

        user, error = self.user_service.register(username, password,email)

        if error:
            return self.render('register', error=error)

        return self.redirect('/login')

    def logout(self):
        return self.redirect('/login')


user_routes = Bottle()
UserController(user_routes)
