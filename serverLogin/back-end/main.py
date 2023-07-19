from configs.config import *
from models.person import *
from routes import *

with app.app_context():

    @app.route("/")
    def inicio():
        return "Back-end operante"

    app.run(debug=True)