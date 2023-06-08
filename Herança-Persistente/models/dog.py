from models.animals import *

class Cachorro(Animal):
    id = db.Column(db.Integer, db.ForeignKey("animal.id"), primary_key = True)

    __mapper_args__ = {
        "polymorphic_identity": "Cachorro"
    }