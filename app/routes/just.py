from flask import Flask, render_template
from flask_login import current_user


def logout():
    return render_template("logout.html")

def loginOk():
    return render_template('login_ok.html')

def base():
    return render_template('base.html')

def signupOk():
    return render_template('signup_ok.html', name=current_user.username)
