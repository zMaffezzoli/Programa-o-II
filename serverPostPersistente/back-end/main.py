from config import *
from people import Pessoa

@app.route("/incluir_pessoas", methods=["post"])
def incluir_pessoas():
    dados = request.get_json()

    resposta = jsonify({"resultado":"Tudo certo! :)"})
    try:
        db.create_all()
        nova_pessoa = Pessoa(**dados)
        db.session.add(nova_pessoa)
        db.session.commit()

    except Exception as error:
         resposta = jsonify({"resultado": "Erro!", "detalhes": str(error)})

    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 

@app.route("/listar_pessoas")
def listar_pessoas():
    pessoas_json = []
    pessoas = db.session.query(Pessoa).all()
    for x in pessoas:
        pessoas_json.append(x.json())

    resposta = jsonify(pessoas_json)

    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
    
app.run(debug=True)