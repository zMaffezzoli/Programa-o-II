from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from models.people import Pessoa

app = Flask(__name__)
CORS(app)

dados_lista = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/incluir")
def incluir_pessoas():
    return render_template("form.html")

@app.route("/listar")
def listar_pessoas():
    return render_template("listar.html")

@app.route("/dados_receber", methods=["POST"])
def dados_receber():
    dados = request.get_json()

    try:
        nova_pessoa = Pessoa(**dados).json()
        dados_lista.append(nova_pessoa)
        return jsonify({"resultado": "Tudo certo! :)"})

    except Exception as error:
        return jsonify({"resultado": "Erro!", "detalhes": str(error)})

@app.route("/dados_enviar")
def dados_enviar():
    return jsonify(dados_lista)

app.run(debug=True)