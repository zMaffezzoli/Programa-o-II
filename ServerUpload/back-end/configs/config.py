from flask import Flask, jsonify, request, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

caminho = os.path.dirname(os.path.abspath(__file__))
caminhopai = os.path.dirname(caminho)
pasta = os.path.join(caminhopai, "database/")
arquivobd = os.path.join(pasta, "data.db")

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)