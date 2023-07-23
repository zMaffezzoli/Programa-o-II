from configs.config import *
from configs.cripto import *
from models.person import *

@app.route("/login", methods=['POST'])
def login():
    dados = request.get_json()
    login = dados["login"]
    senha = dados["senha"]

    encontrar = Pessoa.query.filter_by(login=login, senha=cifrar(senha)).first()
    
    if encontrar is None:
        resposta =  jsonify({"resultado": "Erro! ", "detalhes": "Usuário ou senha incorreto(s)"})

    else: 
        access_token = create_access_token(identity=login)
        resposta = jsonify({"resultado": "ok", "detalhes": access_token})

    return resposta