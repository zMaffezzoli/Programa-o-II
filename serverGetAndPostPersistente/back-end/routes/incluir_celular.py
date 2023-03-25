from configs.config import *
from models import *

@app.route("/incluir_celular", methods=['post'])
def incluir_celular():
    dados = request.get_json()
    try:
        novo_celular = Celular(**dados)
        db.session.add(novo_celular)
        db.session.commit()
        resposta = jsonify({"resultado": "Tudo certo! :)"})

    except Exception as error:
         resposta = jsonify({"resultado": "Erro!", "detalhes": str(error)})

    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 