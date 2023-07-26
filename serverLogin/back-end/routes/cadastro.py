from configs.config import *
from configs.cripto import *
from models.person import *

@app.route("/cadastro/<string:classe>", methods=["POST"])
def cadastro(classe):

    dados = request.get_json()
    dados["senha"] = cifrar(dados["senha"])
    login = dados["login"]
    busca = Pessoa.query.filter_by(login=login).first()
    
    try:
        nova = None
        if classe == "Pessoa":
            nova = Pessoa(**dados)

        db.session.add(nova)
            
    except Exception as e:
        resposta = jsonify({"resultado": "Erro! ", "detalhes": str(e)})
        return resposta

    if busca is None:
        db.session.commit()
        resposta = jsonify({"resultado": "ok"})
        return resposta

    else:
        resposta = jsonify({"resultado": "Erro! ", "detalhes": "Login já existente!"})
        return resposta