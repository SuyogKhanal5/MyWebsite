from flask import Flask
from .views import views
from flask_sqlalchemy import SQLAlchemy
import os
from os import path

# db = SQLAlchemy()
# DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "funny"
    # app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    # db.init_app(app)

    # create_database(app)

    app.register_blueprint(views, url_prefix = "/")

    return app

# def create_database(app):
#     if path.exists("website/" + DB_NAME):
#         os.remove("website/" + DB_NAME)

#     db.create_all(app=app)
#     print("Created Database!")