from app import create_app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = create_app()
class Utilisateur(db.Model):
    __tablename__ = 'utilisateur'
    id = db.Column(db.Integer, primary_key = True)
    Nom = db.Column(db.String(50), nullable = False)
    Prenom = db.Column(db.String(50), nullable = False)
    Mail = db.Column(db.String(40), nullable = False)
    Password = db.Column(db.String(128), nullable = False) 
with app.app_context():
    db.create_all()

if __name__ == "__main__":
   
    app.run(debug=True)
