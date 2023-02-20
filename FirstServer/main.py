from flask import Flask
from people import *

lista = [p1, p2, p3]
app = Flask(__name__)

@app.route("/")
def index():
    return f"<h1>Página primária</h1><a href='http://127.0.0.1:5000/pagina2'>Clique aqui para acessar a página secundária</a>"

@app.route("/pagina2")
def pagina2():
    yield f"<h1>Página secundária</h1>"

    for i in lista:
        yield f"<p>Nome: {i.nome}, idade: {i.idade} anos, cidade: {i.cidade}</p>"
        
    yield f"<a href='http://127.0.0.1:5000/'>Clique aqui para voltar a página principal</a>"

app.run(debug=True)