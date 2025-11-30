from bottle import Bottle, request
from .base_controller import BaseController
from services.jogo_service import JogoService
import json
import os

class JogoController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.jogo_service = JogoService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/jogos', method='GET', callback=self.list_jogos)
        self.app.route('/jogos/add', method=['GET', 'POST'], callback=self.add_jogo)
        self.app.route('/jogos/edit/<jogo_id:int>', method=['GET', 'POST'], callback=self.edit_jogo)
        self.app.route('/jogos/delete/<jogo_id:int>', method='POST', callback=self.delete_jogo)
        self.app.route('/jogo/<jogo_id:int>', 'GET', self.jogo_detalhe)

    @staticmethod
    def carregar_jogos():
        caminho = os.path.join("data", "jogos.json")
        with open(caminho, "r", encoding="utf-8") as f:
            return json.load(f)

    def list_jogos(self):
        jogos = self.jogo_service.listar_jogos()
        return self.render('jogos', jogos=jogos)

    def add_jogo(self):
        if request.method == 'GET':
            return self.render('jogo_form', jogo=None, action='/jogos/add')
        else:
            nome = request.forms.get('nome')
            preco = float(request.forms.get('preco'))
            genero = request.forms.get('genero')
            imagem = request.forms.get('imagem')

            self.jogo_service.adicionar_jogo(nome, preco, genero, imagem)
            return self.redirect('/jogos')

    def edit_jogo(self, jogo_id):
        jogo = self.jogo_service.get_by_id(jogo_id)

        if request.method == 'GET':
            return self.render('jogo_form', jogo=jogo, action=f'/jogos/edit/{jogo_id}')
        else:
            nome = request.forms.get('nome')
            preco = float(request.forms.get('preco'))
            genero = request.forms.get('genero')
            imagem = request.forms.get('imagem')

            self.jogo_service.atualizar(jogo_id, nome, preco, genero, imagem)
            return self.redirect('/jogos')

    def jogo_detalhe(self, jogo_id):
        jogo = self.jogo_service.get_by_id(jogo_id)

        if not jogo:
            return "Jogo não encontrado"

        return self.render('jogo', jogo=jogo)

    def delete_jogo(self, jogo_id):
        self.jogo_service.remover_jogo(jogo_id)
        return self.redirect('/jogos')

jogo_routes = Bottle()
JogoController(jogo_routes)