from flask import Flask, jsonify, request
from flask_cors import CORS
from people import *

app = Flask(__name__)
CORS(app)

@app.route("/incluir_pessoas", methods=['POST'])
def incluir_pessoa():
    dados = request.get_json()

    try:
        nova_pessoa = Pessoa(**dados)
        return jsonify({"resultado": "Tudo certo! :)"})

    except Exception as error:
        return jsonify({"resultado": "Erro!", "detalhes": str(error)})

app.run(debug=True)