from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)


caminho = os.path.dirname(os.path.abspath(__file__))
caminhopai = os.path.dirname(caminho)
arquivobd = os.path.join(caminhopai, 'database/')
arquivobd2 = os.path.join(arquivobd, "dados.db")

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd2
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)