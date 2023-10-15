from configs.config import *
from models.person import *

# curl localhost:5000/listar/Pessoa
@app.route("/listar/<string:classe>")
def listar(classe):

    try: 
        dados = None
        dados_json = []

        if classe == "Pessoa":
            dados = db.session.query(Pessoa).all()

        if dados:
            for x in dados:
                dados_json.append(x.json())
            
            resposta = jsonify({"resultado": "ok", "detalhes": dados_json})

        else:
            resposta = jsonify({"resultado": "Erro!", "detalhes": "Sem dados"})

    except Exception as e:
        resposta = jsonify({"resultado": "Erro! ", "detalhes": str(e)})
        
    return resposta