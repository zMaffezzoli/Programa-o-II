from flask import Flask, jsonify
from people import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    lista = [Pessoa("Fulano", 19, "Pomerode", "24/09/2003").json(), Pessoa("Fulaninho", 9, "Jaraguá do Sul", "12/10/2013").json(), Pessoa("Fulanão", 67, "Timbó", "06/06/1955").json()]
    
    return jsonify(lista)

app.run(debug=True)