from configs.config import *

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text)
    nome_file = db.Column(db.Text)

    def __str__(self):
        return f"Id: {self.id} Nome: {self.nome} Nome_file: {self.nome_file}"

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "nome_file": self.nome_file
        }