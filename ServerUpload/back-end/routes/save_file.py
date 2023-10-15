from configs.config import *


# curl -i -X POST -F files=@foto.jpeg localhost:5000/save_file
@app.route("/save_file", methods=["post"])
def save_file():

    try:
        file = request.files["files"]
        caminho_salvar = os.path.join(caminhopai, "files/" + file.filename)
        file.save(caminho_salvar)
        resposta = jsonify({"resultado":"ok", "detalhes": file.filename})

    except Exception as erro:
        resposta = jsonify({"resposta": "Erro!", "detalhes": str(erro)})

    return resposta