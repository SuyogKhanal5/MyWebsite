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

@views.route("/projects")
def projects():
    return render_template("projects.html")

@views.route("discordsoundboard")
def discordsoundboard():
    return redirect("https://github.com/SuyogKhanal5/DiscordSoundBoard")

    
@views.route("flameracing")
def flameracing():
    return redirect("https://github.com/SuyogKhanal5/FlameRacing")

@views.route("humanbot")
def humanbot():
    return redirect("https://github.com/SuyogKhanal5/HumanBot")

@views.route("subreddit")
def subreddit():
    return redirect("https://github.com/SuyogKhanal5/DiscordSubredditScraper")

@views.route("this-website")
def thiswebsite():
    return redirect("https://github.com/SuyogKhanal5/NewWebsite")