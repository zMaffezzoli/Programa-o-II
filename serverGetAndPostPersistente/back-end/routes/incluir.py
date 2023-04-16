from configs.config import *
from models import *

@app.route("/incluir/<string:classe>", methods=["post"])
def incluir(classe):
    dados = request.get_json()

    try:
        nova = None
        if classe == "Pessoa":
            nova = Pessoa(**dados)
        elif classe == "Celular":
            nova = Celular(**dados)
        db.session.add(nova)
        db.session.commit()
        resposta = jsonify({"resultado": "ok"})

    except Exception as error:
         resposta = jsonify({"resultado": "Erro!", "detalhes": str(error)})

    return resposta 