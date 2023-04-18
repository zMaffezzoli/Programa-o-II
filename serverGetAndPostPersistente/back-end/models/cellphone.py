from configs.config import *
from models.person import *

class Celular(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.Text)
    marca = db.Column(db.Text)
    proprietario_id = db.Column(db.Integer, db.ForeignKey(Pessoa.id), nullable=False)
    proprietario = db.relationship("Pessoa")

    def __str__(self):
        return f"Id: {self.id}, Modelo: {self.modelo}, Marca: {self.marca}, Proprietário:  {self.proprietario.nome}"

    def json(self):
        return{
            "id": self.id,
            "modelo": self.modelo,
            "marca": self.marca,
            "proprietario": self.proprietario.json()
        }