from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint, session
from app.models import Utilisateur
from werkzeug.security import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user
verif = Blueprint("verification", __name__)

db = SQLAlchemy()


@verif.route('/signup_ok')
def signup_ok():
    return render_template("signup_ok.html")

@verif.route('/login_')
def login_():
    return render_template('login_ok.html')


@verif.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        nom = request.form.get('Nom')
        prenom = request.form.get('Prenom')
        mail = request.form.get('Mail')
        password = request.form.get('Password')
        
        new_utilisateur = Utilisateur(Nom = nom, Prenom = prenom, Mail = mail, Password = password)
        db.session.add(new_utilisateur)
        db.session.commit()
        return redirect(url_for('login'))

    else : 
        return render_template('signup.html')
    

@verif.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        verif_mail = request.form.get('Mail')
        verif_password = request.form.get('Password')
        utilisateur = Utilisateur.query.filter_by(Mail= verif_mail, Password= verif_password).first()
        if utilisateur:
            if (utilisateur.Password, verif_password):
                flash('Connexion reussie', category='success')
                return redirect(url_for('login_'))
            else:
                 flash('Erreur veuillez verifier vos informations', category='error')
        else:
            flash('Votre mail est inexistant', category='error')
        return render_template("login.html")
    
@verif.route('/logout')     
def logout():
    return redirect (url_for('logout'))
