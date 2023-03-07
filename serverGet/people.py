class Pessoa:
    def __init__(self, nome, idade, cidade, data):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.data = data

    def __str__(self):
        return f"Nome: {self.nome} Idade: {self.idade} Cidade: {self.cidade} Data de nascimento: {self.data}"

    def json(self):
        return {
            "nome": self.nome,
            "idade": self.idade,
            "cidade": self.cidade,
            "data": self.data
        }