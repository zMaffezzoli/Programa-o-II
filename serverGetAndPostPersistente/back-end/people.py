from config import *

with app.app_context():
    class Pessoa(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        nome = db.Column(db.Text)
        idade = db.Column(db.Text)
        cidade = db.Column(db.Text)
        data = db.Column(db.Text)

        def __str__(self):
            return f"Id: {self.id} Nome: {self.nome} Idade: {self.idade} Cidade: {self.cidade} Data de nascimento: {self.data}"

        def json(self):
            return {
                "id": self.id,
                "nome": self.nome,
                "idade": self.idade,
                "cidade": self.cidade,
                "data": self.data
            }

    # teste    
    if __name__ == "__main__":
        # apagar o arquivo, se houver
        if os.path.exists(arquivobd):
            os.remove(arquivobd)

        # criar tabelas
        db.create_all()

        # teste da classe Pessoa
        p1 = Pessoa(nome="Joao", idade="30", cidade="natal", data="13/03")
        p2 = Pessoa(nome="Joaozinho", idade="20", cidade="Recife", data="05/03")

        # persistir
        db.session.add(p1)
        db.session.add(p2)
        db.session.commit()
        
        # exibir a pessoa
        print(p2)

        # exibir a pessoa no format json
        print(p2.json())

        print(db.session.query(Pessoa).all())