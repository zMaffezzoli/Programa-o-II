from configs.config import *

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.Text)
    raca = db.Column(db.Text)
    cor = db.Column(db.Text)
    genero = db.Column(db.Text)
    tipo = db.Column(db.Text)

    __mapper_args__ = {
        "polymorphic_identity": "Animal",
        "polymorphic_on": tipo
    }