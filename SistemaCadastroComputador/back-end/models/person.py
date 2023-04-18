from configs.config import *

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text)
    email = db.Column(db.Text)
    sexo = db.Column(db.Text)
    data_nascimento = db.Column(db.Text)

    def __str__(self):
        return f"Id: {self.id}, Nome: {self.nome}, Email: {self.email}, Sexo: {self.sexo}, Data de nascimento: {self.data_nascimento}"

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "sexo": self.sexo,
            "data_nascimento": self.data_nascimento
        }