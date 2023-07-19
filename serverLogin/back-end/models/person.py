from configs.config import *

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.Text)
    senha = db.Column(db.Text)

    def __str__(self):
        return f"Id: {self.id} Login: {self.login} Senha: {self.senha}"

    def json(self):
        return {
            "id": self.id,
            "login": self.login,
            "senha": self.senha
        }