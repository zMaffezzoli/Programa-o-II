from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from models.people import Pessoa

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/incluir_pessoas", methods=['POST'])
def incluir_pessoa():
    dados = request.get_json()

    try:
        nova_pessoa = Pessoa(**dados)
        return jsonify({"resultado": "Tudo certo! :)"})

    except Exception as error:
        return jsonify({"resultado": "Erro!", "detalhes": str(error)})

app.run(debug=True)