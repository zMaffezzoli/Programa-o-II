from configs.config import *
from models.person import *

class Computador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    placa_mae = db.Column(db.Text)
    processador = db.Column(db.Text)
    placa_video = db.Column(db.Text)
    fonte = db.Column(db.Text)
    memoria_ram = db.Column(db.Text)
    proprietario_id = db.Column(db.Integer, db.ForeignKey(Pessoa.id), nullable=False)
    proprietario = db.relationship("Pessoa")

    def __str__(self):
        return f"Id: {self.id}, Placa mãe: {self.placa_mae}, Processador: {self.processador}, Placa de vídeo: {self.placa_video}, Fonte: {self.fonte}W, Memória ram: {self.memoria_ram}GB, Proprietário: {self.proprietario.nome}"

    def json(self):
        return {
            "id": self.id,
            "placa_mae": self.placa_mae,
            "processador": self.processador,
            "placa_video": self.placa_video,
            "fonte": self.fonte,
            "memoria_ram": self.memoria_ram,
            "proprietario": self.proprietario.json()
        }
