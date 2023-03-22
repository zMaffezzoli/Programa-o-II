from configs.config import *

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text)
    idade = db.Column(db.Text)
    cidade = db.Column(db.Text)
    data = db.Column(db.Text)

    def __str__(self):
        return f"Id: {self.id} Nome: {self.nome} Idade: {self.idade} Cidade: {self.cidade} Data de nascimento: {self.data}"

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "cidade": self.cidade,
            "data": self.data
        }