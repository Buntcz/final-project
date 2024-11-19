import os

from flask import Flask, render_template,redirect,request,session
from flask_session import Session
from werkzeug.security import check_password_hash,generate_password_hash
from cs50 import SQL
from helpers import apology,login_required

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///app.db")

@app.after_request
def after_requests(response):
    response.headers["Cache-control"] = "no-cache, no-store, must-validate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/login", methods=["GET", "POST"])
def login():

    session.clear()

    if request.method == "POST":
        if not request.form.get("username"):
            apology("Please provide a username")
        elif not request.form.get("password"):
            return apology("Please provide a password")
        
        rows = db.execute("SELECT * FROM users WHERE username = (?)", request.form.get("username"))
        if len(rows) !=1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("Invalid username or password")
        
        session["user_id"] = rows[0]["id"]

        return redirect("/")
    else:
        return render_template("login.html")


@app.route("/")
@login_required
def index():
    user_id = session["user_id"]
    username = db.execute("SELECT username FROM users WHERE id = (?)", user_id)

    return render_template("index.html", user=username[0]["username"])

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        user = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        users = db.execute("SELECT username FROM users")
        if not user:
            return apology("No username provided")
        for username in users:
            if user == username["username"]:
                return apology("Username already in use")
        if not password or not confirmation:
            return apology("Please provide both password and confirmation for it")
        if password != confirmation:
            return apology("passwords do not match")
        pass_hash = generate_password_hash(password)
        db.execute("INSERT INTO users (username,hash) VALUES(?,?)", user,pass_hash)
        return redirect("/login")
    else:
        return render_template("register.html")


@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        user_id = session["user_id"]
        location = request.form.get("location")
        price = request.form.get("price")
        mood = request.form.get("mood")
        desc = request.form.get("desc")
        if not location:
            return apology("Please enter the location you have visited")
        if not desc:
            return apology("Please describe how you spent your holiday/vacation")
        db.execute("INSERT INTO posts(location,price,mood,desc,user_id) VALUES(?,?,?,?,?)", location,price,mood,desc,user_id)
        return redirect("/")
    else:
        return render_template("create.html")

@app.route("/myaccount", methods=["GET","POST"])
def myaccount():
    user_id = session["user_id"]
    posts = db.execute("SELECT * FROM posts WHERE user_id == (?)", user_id)
    user = db.execute("SELECT username FROM users WHERE id == (?)", user_id)
    return render_template("myaccount.html", user = user[0]["username"], posts = posts)

@app.route("/home", methods=["GET"])
def home():
    posts = db.execute("SELECT * FROM posts ORDER BY post_id DESC LIMIT 10")
    return render_template("home.html", posts = posts)

@app.route("/delete", methods=["POST","GET"])
def delete():
    post_id = request.form.get("post_id")
    db.execute("DELETE FROM posts WHERE post_id == (?)", post_id)
    return redirect("/myaccount")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")
