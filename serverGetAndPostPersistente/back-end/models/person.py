from configs.config import *

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text)
    idade = db.Column(db.Integer)
    cidade = db.Column(db.Text)
    data_nascimento = db.Column(db.Text)

    def __str__(self):
        return f"Id: {self.id} Nome: {self.nome} Idade: {self.idade} Cidade: {self.cidade} Data de nascimento: {self.data_nascimento}"

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "cidade": self.cidade,
            "data_nascimento": self.data_nascimento
        }