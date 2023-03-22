from configs.config import *
from models.person import *

@app.route("/listar_pessoas")
def listar_pessoas():
    pessoas_json = []
    pessoas = db.session.query(Pessoa).all()
    for x in pessoas:
        pessoas_json.append(x.json())

    resposta = jsonify(pessoas_json)

    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta