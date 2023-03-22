from configs.config import *
from models.person import *

@app.route("/incluir_pessoas", methods=["post"])
def incluir_pessoas():
    dados = request.get_json()

    try:
        nova_pessoa = Pessoa(**dados)
        db.session.add(nova_pessoa)
        db.session.commit()
        resposta = jsonify({"resultado": "Tudo certo! :)"})

    except Exception as error:
         resposta = jsonify({"resultado": "Erro!", "detalhes": str(error)})

    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 