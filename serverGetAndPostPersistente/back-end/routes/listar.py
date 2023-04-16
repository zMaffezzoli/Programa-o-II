from configs.config import *
from models import *

@app.route("/listar/<string:classe>")
def listar(classe):
    dados = None
    if classe == "Pessoa":
        dados = db.session.query(Pessoa).all()
    elif classe == "Celular":
        dados = db.session.query(Celular).all()
    if dados:
        dados_json = []
        for x in dados:
            dados_json.append(x.json())

        meujson = {"resultado": "ok", "detalhes": dados_json}
        return jsonify(meujson)

    elif dados == []:
        return jsonify({"resultado": "Erro!", "detalhes": "Sem dados."})
    
    else:
        return jsonify({"resultado": "Erro!", "detalhes": "Classe informada inválida: "+classe})