from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.routes.verification import *
from app.routes.just import *
from os import path
from .models import Utilisateur
from flask_login import LoginManager, login_required

db_name = "mydatabase.sqlite"
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.secret_key = "it_is_secret"

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.sqlite'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False   
    db.init_app(app)
    
    
    app.route('/logout')(logout)
    app.route('/login_')(login_)
    app.route('/login', methods=['GET', 'POST'])(login)
    app.route('/signup', methods=['GET', 'POST'])(signup)
    app.route('/login_ok', methods=['GET', 'POST'])(login_required(loginOk))
    app.route('/sigup_ok', methods=['GET', 'POST'])(login_required(signupOk))    
    app.route('/', methods=["GET",])(base)
  
    
    login_manager = LoginManager()
    login_manager.login_view = 'login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(utilisateur_id):
        utilisateur = Utilisateur.query.filter_by(id=utilisateur_id).first()
        return Utilisateur.query.get(int(utilisateur_id))

    return app

def create_database(app):    
    db.create_all(app=app)
