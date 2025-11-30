# controllers/games_controller.py
from models.jogo import Jogo
from bottle import template # Certifique-se de importar o 'template'

class GamesController:
    def __init__(self, app):
        self.app = app
        self._setup_routes()

    def _setup_routes(self):
        self.app.route('/games', method='GET', callback=self.listar_jogos)
        # Rota para a página de detalhes de um único jogo
        self.app.route('/games/<id_jogo:int>', method='GET', callback=self.detalhes_jogo) # NOVO

    def buscar_jogo_por_id(self, id_alvo):
        # Reutiliza o carregamento de todos os jogos
        todos_jogos = self.carregar_jogos() 
        
        # Itera sobre a lista para encontrar o jogo com o ID correspondente
        for jogo in todos_jogos:
            if jogo.id == id_alvo:
                return jogo
        
        # Retorna None ou levanta uma exceção se o jogo não for encontrado
        return None

    # controllers/games_controller.py (ADIÇÃO NECESSÁRIA)

# ... (outros métodos)

    # 1. Este método é o que estava faltando e causava o crash na inicialização
    def listar_jogos(self):
        # Assume que 'template' está importado no topo do arquivo.
        jogos = self.carregar_jogos()
        # Se você tinha uma página /games separada que listava todos os jogos
        return template('games', jogos=jogos) 
        
    def carregar_jogos(self):
        # 1. Defina o caminho correto para o seu JSON (Aquele que você descobriu que funcionava)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        path_json = os.path.normpath(os.path.join(current_dir, "../data/jogos.json"))
        
        # Lista onde os objetos Jogo serão armazenados
        lista_jogos = []
        
        try:
            # 2. Tenta abrir o arquivo
            with open(path_json, 'r', encoding='utf-8') as f:
                dados = json.load(f)
            
            # 3. Itera sobre os dados para criar objetos Jogo
            for item in dados:
                # Garanta que os nomes dos campos (id, nome, etc.) estão corretos conforme sua classe Jogo
                jogo = Jogo(
                    id=item['id'],
                    nome=item['nome'],
                    preco=item['preco'],
                    descricao=item['descricao'],
                    # Adicione todos os outros atributos que a classe Jogo espera
                )
                lista_jogos.append(jogo)
                
            return lista_jogos # Retorna a lista de objetos Jogo

        except FileNotFoundError:
            print(f"ERRO: Arquivo JSON não encontrado no caminho: {path_json}")
            return [] # <--- CRUCIAL: Retorna lista vazia em caso de FALHA, não None
        except json.JSONDecodeError:
            print("ERRO: O arquivo jogos.json está mal formatado (JSON inválido).")
            return [] # <--- CRUCIAL: Retorna lista vazia em caso de JSON inválido
        except Exception as e:
            print(f"Erro desconhecido ao carregar jogos: {e}")
            return [] # <--- CRUCIAL
    
# ... (restante da classe, detalhes_jogo, etc.)

    def detalhes_jogo(self, id_jogo):
        jogo = self.buscar_jogo_por_id(id_jogo)
        
        if jogo:
            # Renderiza o template 'detalhes_jogo' passando o objeto 'jogo'
            return template('detalhes_jogo', jogo=jogo)
        else:
            # Trata o caso de jogo não encontrado
            return "Erro 404: Jogo não encontrado.", 404 

    # ... (restante da classe)