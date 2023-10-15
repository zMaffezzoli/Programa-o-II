from configs.config import *
from models.person import *

# curl localhost:5000/incluir/Pessoa -X POST -d '{"nome": "Pedrinho", "nome_file": "foto.jpeg"}' -H "Content-Type:application/json"
@app.route("/incluir/<string:classe>", methods=["post"])
def incluir(classe):
    dados = request.get_json()

    try:
        nova = None
        if classe == "Pessoa":
            nova = Pessoa(**dados)

        db.session.add(nova)
        db.session.commit()
        resposta = jsonify({"resultado": "ok"})

    except Exception as error:
        resposta = jsonify({"resultado": "Erro!", "detalhes": str(error)})

    return resposta