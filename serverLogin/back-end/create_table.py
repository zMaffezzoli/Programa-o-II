from configs.config import *
from configs.cripto import *
from models.person import *

p1 = Pessoa(login = "admin", senha = cifrar("admin"))

with app.app_context():

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()
    db.session.add(p1)
    db.session.commit()