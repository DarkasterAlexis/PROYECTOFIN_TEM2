from flask import Flask, request,render_template,redirect,url_for
from flask_login import LoginManager,login_required, logout_user, login_user,UserMixin,current_user
from database import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pedidos.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

