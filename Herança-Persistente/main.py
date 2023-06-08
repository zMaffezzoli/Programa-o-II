from configs.config import *
from models import *

with app.app_context():
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    gato1 = Gato(nome = "Lola", cor = "Cinza", genero = "Fêmea", fugas = 0)
    gato2 = Gato(nome = "Cacau", raca = "Siamês", cor = "Mescla", genero = "Fêmea", fugas = 5)
    cachorro1 = Cachorro(nome = "Brutus", raca = "Pitbull", cor = "Branco", genero = "Macho")

    db.session.add(gato1)
    db.session.add(cachorro1)
    db.session.add(gato2)
    db.session.commit()