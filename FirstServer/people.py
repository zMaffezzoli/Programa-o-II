class Pessoa:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def __str__(self):
        return f"Nome: {self.nome} Idade: {self.idade} Cidade: {self.cidade}"

    def json(self):
        return {
            "Nome": self.nome,
            "Idade": self.idade,
            "Cidade": self.cidade
        }