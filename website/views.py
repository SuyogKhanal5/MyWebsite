from flask import render_template, Blueprint, redirect, flash, request
import praw
import random
# from .models import Posts
# from . import db

views = Blueprint("views", __name__)

reddit = praw.Reddit(
                    client_id = '_-ejRHCzo21uZ4kSBxswNg', 
                    client_secret = 'VvgMAA9mGx0n5nxFj-W7ayxGRYvR4Q', 
                    username = 'RedditScrapingAlt', 
                    password = 'scrapingredditalt', 
                    user_agent = 'DiscordScraper')

post_text = ""

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
    return redirect("https://github.com/SuyogKhanal5/MyWebsite")

@views.route("reddit", methods = ["GET","POST"])
def reddit():
    if request.method == "POST":
        text = request.form.get("text")
        if not text:
                flash("Subreddit cannot be empty", category = "error")
                return render_template("reddit.html")
        else:
            post_text = text
            return render_template("returnposts.html")
    else:
        return render_template("reddit.html")

@views.route("returnpost", methods = ["GET","POST"])
def returnpost():
    text = post_text
            
    subreddit = reddit.subreddit(text)

    all_submissions = []

    hot = subreddit.hot(limit = 50)

    names_list = []
    author_list = []
    submission_desc_list = []
    link_list = []       
            
    for submission in hot:
        all_submissions.append(submission)

        random_submission = random.choice(all_submissions)
                
        names_list.append(random_submission.title)
        author_list.append(random_submission.author)
        submission_desc_list.append(random_submission.selftext)
        link_list.append('https://www.reddit.com' + random_submission.permalink)

        # post = Posts.query_filterby(title = name, author = author, body = submission_desc, link = link)

        # db.session.add(post)
        # db.session.commit()        

    return render_template("returnposts.html", names = names_list, author = author_list, submission_desc = submission_desc_list, link = link_list)