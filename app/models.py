from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()
app = Flask(__name__)



class Utilisateur(db.Model):
    __tablename__ = 'utilisateur'
    id = db.Column(db.Integer, primary_key = True)
    Nom = db.Column(db.String(50), nullable = False)
    Prenom = db.Column(db.String(50), nullable = False)
    Mail = db.Column(db.String(40), nullable = False)
    Password = db.Column(db.String(128), nullable = False)   
    

