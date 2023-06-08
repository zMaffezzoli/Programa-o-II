from models.animals import *

class Gato(Animal):
    id = db.Column(db.Integer, db.ForeignKey("animal.id"), primary_key = True)
    fugas = db.Column(db.Integer)

    __mapper_args__ = {
        "polymorphic_identity": "Gato"
    }