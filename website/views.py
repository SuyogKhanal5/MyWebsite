from flask import render_template, Blueprint, redirect, flash, request
import praw

views = Blueprint("views", __name__)

reddit = praw.Reddit(
                    client_id = '_-ejRHCzo21uZ4kSBxswNg', 
                    client_secret = 'VvgMAA9mGx0n5nxFj-W7ayxGRYvR4Q', 
                    username = 'RedditScrapingAlt', 
                    password = 'scrapingredditalt', 
                    user_agent = 'DiscordScraper')

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

@views.route("reddit")
def reddit():
    if request.method == "POST":
        text = request.form.get("text")
        if not text:
                flash("Subreddit cannot be empty", category = "error")
                return render_template("reddit.html")
    else:
        return render_template("reddit.html")

@views.route("returnpost", methods = ["GET","POST"])
def returnpost():
            subreddit = reddit.subreddit(text)

            all_submissions = []

            hot = subreddit.hot(limit = 50)
            
            for submission in hot:
                all_submissions.append(submission)

            random_submission = random.choice(all_submissions)
                    
            class Post:
                name = random_submission.title
                submission_url = random_submission.url
                submission_desc = random_submission.selftext
                link = 'https://www.reddit.com' + random_submission.permalink
            
            post = Post(name, submission_url, submission_desc, link)

            flash("Success", category = "success")

            return render_template("returnposts.html", post)