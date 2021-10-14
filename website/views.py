from flask import render_template, Blueprint

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html")

@views.route("/updates")
def updates():
    return render_template("updates.html")