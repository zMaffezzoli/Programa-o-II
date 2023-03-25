from configs.config import *
from models import *

@app.route("/listar_celular")
def listar_celular():
    celulares_json = []
    celulares = db.session.query(Celular).all()
    for x in celulares:
        celulares_json.append(x.json())

    resposta = jsonify(celulares_json)

    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta