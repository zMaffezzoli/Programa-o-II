from configs.config import *
from models.person import *

# curl localhost:5000/get_file/1
@app.route("/get_file/<int:id_pessoa>")
def get_file(id_pessoa):
    pessoa = db.session.get(Pessoa, id_pessoa)
    file = os.path.join(caminhopai, "files/" + pessoa.nome_file)
    return send_file(file)