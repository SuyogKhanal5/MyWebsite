from flask import render_template, Blueprint, redirect

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html")

@views.route("/updates")
def updates():
    return render_template("updates.html")

@views.route("/suyog")
def suyog():
    return render_template("suyog.html")

@views.route("twitter")
def twitter():
    return redirect("https://twitter.com/SuyogKhanal555")

@views.route("github")
def github():
    return redirect("https://github.com/SuyogKhanal5")