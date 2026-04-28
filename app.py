from flask import Flask
from flask import abort, flash, make_response, redirect, render_template, request, session
from werkzeug.security import generate_password_hash
from secrets import token_hex
import markupsafe
import config
import entries
import users


app = Flask(__name__)
app.secret_key = config.secret_key

def check_csrf(csrf_token):
    if csrf_token != session["csrf_token"]:
        abort(403)

def check_user(user_id):
    if user_id != session["user_id"]:
        abort(403)

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

def check_message(content):
    if not content or len(content) > 250:
        abort(403)

@app.template_filter()
def show_lines(content):
    content = str(markupsafe.escape(content))
    content = content.replace("\n", "<br />")
    return markupsafe.Markup(content)

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
def show_entry(entry_id):
    entry = entries.get_entry(entry_id)
    if not entry:
        abort(404)
    classes = entries.get_classes(entry_id)
    discussion = entries.get_discussion(entry_id)
    images = entries.get_images(entry_id)
    return render_template("show_entry.html", entry=entry, classes=classes, discussion=discussion, images=images, session=session)

@app.route("/new_entry")
def new_entry():
    require_login()
    classes = entries.get_all_classes()
    return render_template("new_entry.html", classes=classes, session=session)

@app.route("/create_entry", methods=["POST"])
def create_entry():
    require_login()

    title = request.form["title"]
    artist = request.form["artist"]
    comment = request.form["comment"]
    user_id = session["user_id"]
    csrf_token = request.form["csrf_token"]

    all_classes = entries.get_all_classes()

    classes = []
    for option in request.form.getlist("classes"):
        if option:
            c_title, c_value = option.split(":")
            if c_title not in all_classes:
                abort(403)
            if c_value not in all_classes[c_title]:
                abort(403)
            classes.append((c_title, c_value))

    check_csrf(csrf_token)

    check_length(title, artist, comment)
    entries.new_entry(title, artist, comment, user_id, classes)

    return redirect("/")

@app.route("/edit_entry/<int:entry_id>")
def edit_entry(entry_id):
    require_login()
    entry = entries.get_entry(entry_id)
    if not entry:
        abort(404)
    if entry["user_id"] != session["user_id"]:
        abort(403)

    all_classes = entries.get_all_classes()
    classes = {}
    for c_class in all_classes:
        classes[c_class] = ""
    for key in entries.get_classes(entry_id):
        classes[key["title"]] = key["value"]

    return render_template("edit_entry.html", entry=entry, all_classes=all_classes, classes=classes, session=session)

@app.route("/update_entry", methods=["POST"])
def update_entry():
    require_login()
    entry_id = request.form["entry_id"]
    csrf_token = request.form["csrf_token"]
    entry = entries.get_entry(entry_id)
    if not entry:
        abort(404)
    check_user(entry["user_id"])
    check_csrf(csrf_token)
    title = request.form["title"]
    artist = request.form["artist"]
    comment = request.form["comment"]
    check_length(title, artist, comment)

    all_classes = entries.get_all_classes()

    classes = []
    for option in request.form.getlist("classes"):
        if option:
            c_title, c_value = option.split(":")
            if c_title not in all_classes:
                abort(403)
            if c_value not in all_classes[c_title]:
                abort(403)
            classes.append((c_title, c_value))

    entries.update_entry(title, artist, comment, entry_id, classes)

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
            csrf_token = request.form["csrf_token"]
            check_csrf(csrf_token)
            if not entry:
                abort(404)
            check_user(entry["user_id"])
            entries.remove_entry(entry_id)
            return redirect("/")
        else:
            return redirect("/entry/" + str(entry_id))

@app.route("/images/<int:entry_id>")
def edit_images(entry_id):
    require_login()
    entry = entries.get_entry(entry_id)
    if not entry:
        abort(404)
    check_user(entry["user_id"])
    images = entries.get_images(entry_id)
    return render_template("images.html", entry=entry, images=images, session=session)

@app.route("/image/<int:image_id>")
def show_image(image_id):
    image = entries.get_image(image_id)
    if not image:
        abort(404)
    response = make_response(bytes(image[0][0]))
    response.headers.set("Content-Type", "image/png")
    return response

@app.route("/add_image", methods=["POST"])
def add_image():
    require_login()
    csrf_token = request.form["csrf_token"]
    entry_id = request.form["entry_id"]
    entry = entries.get_entry(entry_id)

    check_csrf(csrf_token)
    check_user(entry["user_id"])

    alt = request.form["alt"]
    file = request.files["image"]
    if not file.filename.endswith(".png"):
        flash("ERROR: invalid file format")
        return redirect("/images/" + str(entry_id))
    image = file.read()
    if len(image) > 100 * 1024:
        flash("ERROR: invalid file size")
        return redirect("/images/" + str(entry_id))

    entries.add_image(entry_id, image, alt)
    return redirect("/images/" + str(entry_id))

@app.route("/remove_images", methods=["POST"])
def remove_images():
    require_login()
    csrf_token = request.form["csrf_token"]
    entry_id = request.form["entry_id"]
    entry = entries.get_entry(entry_id)
    if not entry:
        abort(404)
    check_csrf(csrf_token)
    check_user(entry["user_id"])

    for image_id in request.form.getlist("image_id"):
        entries.remove_image(entry_id, image_id)

    return redirect("/images/" + str(entry_id))

@app.route("/find_entry")
def find_entry():
    query = request.args.get("query")
    if query:
        results = entries.find_entries(query)
    else:
        query = ""
        results = []
    return render_template("find_entry.html", query=query, results=results)

@app.route("/new_message", methods=["POST"])
def new_message():
    require_login()
    csrf_token = request.form["csrf_token"]
    content = request.form["content"]
    user_id = session["user_id"]
    entry_id = request.form["entry_id"]

    check_csrf(csrf_token)
    check_user(user_id)
    check_message(content)

    entries.add_message(content, user_id, entry_id)
    return redirect("/entry/" + str(entry_id))

@app.route("/edit_message/<int:message_id>", methods=["GET", "POST"])
def edit_message(message_id):
    require_login()
    message = entries.get_message(message_id)
    check_user(message["user_id"])

    if request.method == "GET":
        return render_template("edit_message.html", message=message, session=session)

    if request.method == "POST":
        content = request.form["content"]
        csrf_token = request.form["csrf_token"]
        check_csrf(csrf_token)
        check_message(content)
        entries.update_message(message["id"], content)
        return redirect("/entry/" + str(message["entry_id"]))

@app.route("/remove_message/<int:message_id>", methods=["GET", "POST"])
def remove_message(message_id):
    require_login()
    message = entries.get_message(message_id)
    entry = entries.get_entry(message["entry_id"])
    check_user(message["user_id"])

    if request.method == "GET":
        return render_template("remove_message.html", message=message, entry=entry, session=session)

    if request.method == "POST":
        csrf_token = request.form["csrf_token"]
        check_csrf(csrf_token)
        if "continue" in request.form:
            entries.remove_message(message["id"])
        return redirect("/entry/" + str(message["entry_id"]))

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if len(username) < 4 or len(username) > 16:
        flash("ERROR: username must be 4-16 characters long")
        return render_template("register.html")
    if not password1 or not password2:
        flash("ERROR: please fill all the fields")
        return render_template("register.html")
    if password1 != password2:
        flash("ERROR: passwords don't match")
        return render_template("register.html")
    password_hash = generate_password_hash(password1)

    try:
        users.create_user(username, password_hash)
    except:
        flash("ERROR: username already exists")
        return render_template("register.html")
    flash("Account created successfully")
    return redirect("/")

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
            session["csrf_token"] = token_hex(16)
            return redirect("/")
        else:
            flash("ERROR: invalid login details")
            return render_template("login.html")

@app.route("/logout")
def logout():
    if "user_id" in session:
        del session["user_id"]
        del session["username"]

    return redirect("/")