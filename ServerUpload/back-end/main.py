from configs.config import *
from routes import *

with app.app_context():
    db.create_all()
    app.run(debug=True)