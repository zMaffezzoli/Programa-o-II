from flask import Flask, jsonify
from people import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    lista = [Pessoa("Fulano", 20, "Pomerode").json(), Pessoa("Fulaninho", 10, "Jaraguá do Sul").json(), Pessoa("Fulanão", 68, "Timbó").json()]
    
    return jsonify(lista)

app.run(debug=True)