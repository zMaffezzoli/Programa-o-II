from configs.config import *
from configs.cripto import *
from models.person import *

@app.route("/login", methods=['POST'])
def login():
    dados = request.get_json()
    login = dados["login"]
    senha = dados["senha"]

    encontrarlogin = Pessoa.query.filter_by(login=login).first()
    encontrar = Pessoa.query.filter_by(login=login, senha=cifrar(senha)).first()

    if encontrarlogin is None:
        resposta =  jsonify({"resultado": "Erro! ", "detalhes": "Login incorreto!"})
        return resposta

    elif encontrar is None:
        resposta =  jsonify({"resultado": "Erro! ", "detalhes": "Senha incorreta!"})
        return resposta

    else: 
        access_token = create_access_token(identity=login)
        resposta = jsonify({"resultado": "ok", "detalhes": access_token})
        return resposta