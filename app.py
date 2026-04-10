from flask import Flask
from flask import abort, redirect, render_template, request, session
from werkzeug.security import generate_password_hash, check_password_hash
import config
import entries
import users


app = Flask(__name__)
app.secret_key = config.secret_key

def require_login():
    if "user_id" not in session:
        abort(403)

def check_length(title, artist, comment):
    if not title or len(title) > 100:
        abort(403)
    if not artist or len(artist) > 75:
        abort(403)
    if len(comment) > 2500:
        abort(403)

@app.route("/")
def index():
    all_entries = entries.get_entries()
    return render_template("index.html", entries=all_entries)

@app.route("/user/<int:user_id>")
def show_user(user_id):
    user = users.get_user(user_id)
    if not user:
        abort(404)
    collection = users.get_collection(user_id)
    return render_template("show_user.html", user=user, collection=collection)

@app.route("/entry/<int:entry_id>")
def entry(entry_id):
    entry = entries.get_entry(entry_id)
    if not entry:
        abort(404)
    return render_template("show_entry.html", entry=entry)

@app.route("/new_entry")
def new_entry():
    require_login()
    return render_template("new_entry.html")

@app.route("/create_entry", methods=["POST"])
def create_entry():
    require_login()

    title = request.form["title"]
    artist = request.form["artist"]
    comment = request.form["comment"]
    user_id = session["user_id"]

    check_length(title, artist, comment)
    entries.new_entry(title, artist, comment, user_id)

    return redirect("/")

@app.route("/edit_entry/<int:entry_id>")
def edit_entry(entry_id):
    require_login()
    entry = entries.get_entry(entry_id)
    if not entry:
        abort(404)
    if entry["user_id"] != session["user_id"]:
        abort(403)
    return render_template("edit_entry.html", entry=entry)

@app.route("/update_entry", methods=["POST"])
def update_entry():
    require_login()
    entry_id = request.form["entry_id"]
    entry = entries.get_entry(entry_id)
    if not entry:
        abort(404)
    if entry["user_id"] != session["user_id"]:
        abort(403)
    title = request.form["title"]
    artist = request.form["artist"]
    comment = request.form["comment"]
    check_length(title, artist, comment)
    entries.update_entry(title, artist, comment, entry_id)

    return redirect("/entry/" + str(entry_id))

@app.route("/remove_entry/<int:entry_id>", methods=["GET", "POST"])
def remove_entry(entry_id):
    require_login()

    if request.method == "GET":
        entry = entries.get_entry(entry_id)
        if not entry:
            abort(404)
        if entry["user_id"] != session["user_id"]:
            abort(403)
        return render_template("remove_entry.html", entry=entry)

    if request.method == "POST":
        if "remove" in request.form:
            entry = entries.get_entry(entry_id)
            if not entry:
                abort(404)
            if entry["user_id"] != session["user_id"]:
                abort(403)
            entries.remove_entry(entry_id)
            return redirect("/")
        else:
            return redirect("/entry/" + str(entry_id))

@app.route("/find_entry")
def find_entry():
    query = request.args.get("query")
    print(query)
    if query:
        results = entries.find_entries(query)
    else:
        query = ""
        results = []
    print(results)
    return render_template("find_entry.html", query=query, results=results)

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        return "ERROR: passwords don't match"
    password_hash = generate_password_hash(password1)

    try:
        users.create_user(username, password_hash)
    except:
        return "ERROR: username already exists"

    return "Account created successfully"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user_id = users.check_login(username, password)

        if user_id:
            session["user_id"] = user_id
            session["username"] = username
            return redirect("/")
        else:
            return "ERROR: wrong password or username"

@app.route("/logout")
def logout():
    if "user_id" in session:
        del session["user_id"]
        del session["username"]
    return redirect("/")