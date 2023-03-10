from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from models.people import Pessoa

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/incluir")
def incluir_pessoas():
    return render_template("form.html")

@app.route("/dados", methods=["GET","POST"])
def data():
    dados = request.get_json()

    try:
        nova_pessoa = Pessoa(**dados)
        return jsonify(nova_pessoa.json())

    except Exception as error:
        return jsonify({"resultado": "Erro!", "detalhes": str(error)})

@app.route("/listar")
def listar_pessoas():
    return render_template("listar.html")

app.run(debug=True)