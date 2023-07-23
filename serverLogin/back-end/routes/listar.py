from configs.config import *
from models.person import *

@app.route("/listar/<string:classe>")
@jwt_required()
def listar(classe):

    try: 
        dados = None
        current_user = get_jwt_identity()
        dados_json = []

        if classe == "Pessoa":
            dados = db.session.query(Pessoa).all()

        for x in dados:
            dados_json.append(x.json())
        
        resposta = jsonify({"resultado": "ok", "detalhes": dados_json})

    except Exception as e:
        resposta = jsonify({"resultado": "Erro! ", "detalhes": str(e)})
        
    return resposta