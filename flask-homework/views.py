import re
from app import app
from flask import abort, request, redirect, render_template, session, url_for
import random

users = ["Oleh", "Ivan", "Polina", "Tamara"]

books = ["Kobzar", "1984", "Finansyst, Tytan, Stoik", "Atlant rozpavyv plechi"]

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.get("/")
def home_page():
    if "username" in session:
        return render_template("homepage.html"), 200
    else:
        return redirect(url_for("login"))


@app.get("/users")
def get_users():
    count = int(request.args.get("count")) if request.args.get("count") else random.randint(1, 111)
    random_users = random.choices(users, k=count)
    if "username" in session:
        return render_template("users.html", random_users=random_users), 200
    else:
        return redirect(url_for("login"))


@app.get("/books")
def get_book():
    count = int(request.args.get("count")) if request.args.get("count") else random.randint(1, 111)
    random_books = random.choices(books, k=count)
    if "username" in session:
        return render_template("books.html", random_books=random_books), 200
    else:
        return redirect(url_for("login"))


@app.get("/users/<int:id>")
def get_user_id(id):
    if "username" in session:
        if not id % 2:
            return render_template("user_id.html", id=id), 200
        else:
            abort(404, "Not found")
    else:
        return redirect(url_for("login"))


@app.get("/books/<string:title>")
def get_book_title(title):
    if "username" in session:
        return render_template("book_title.html", title=title.title())
    else:
        return redirect(url_for("login"))


@app.get("/params")
def get_params():
    if "username" in session:
        return render_template("parameters.html", parameters=request.args.items())
    else:
        return redirect(url_for("login"))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session['username'] = request.form['username']

        if not username or not password:
            abort(400, "No information provided")

        if len(username) < 5:
            abort(400, "Username too short.")
        elif len(password) < 8:
            abort(400, "Password too short.")
        elif not re.search(r"\d", password):
            abort(400, "Password must contain at least one digit.")
        elif not re.search(r"[A-Z]", password):
            abort(400, "Password must contain at least one uppercase letter.")

        return redirect('/users')

    else:
        return render_template("login.html", session=session)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


@app.errorhandler(404)
def handle_not_found(e):
    return "<strong>Not found</strong>", 404


@app.errorhandler(500)
def handle_internal_server_error(e):
    return "<h1>Internal server error</h1>", 500
