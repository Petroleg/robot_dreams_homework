import os
import re
from app import app, db
from flask import abort, request, redirect, render_template, session, url_for, jsonify
from models import User, Book, Purchase


app.secret_key = os.getenv('SECRET_KEY')


@app.get("/")
def home_page():
    if "username" in session:
        return render_template("homepage.html"), 200
    else:
        return redirect(url_for("login"))


def check_session():
    if "username" not in session:
        return redirect(url_for("login"))


@app.route('/users', methods=['POST', 'GET'])
def handle_users():
    if request.method == 'POST':
        if request.content_type == 'application/json':
            data = request.json
        elif request.content_type == 'application/x-www-form-urlencoded':
            data = request.form
        else:
            return jsonify({'error': 'Invalid content type'}), 400

        user = User(first_name=data.get('first_name'), last_name=data.get('last_name'), age=data.get('age'))

        db.session.add(user)
        db.session.commit()

        return jsonify({'message': 'User created successfully'}), 201
    elif request.method == 'GET':
        args = request.args.get("size")
        if not args:
            users = User.query.all()
        else:
            users = User.query.limit(int(args)).all()

        user_list = []
        for user in users:
            user_dict = {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "age": user.age,
            }
            user_list.append(user_dict)

        return jsonify(user_list)


@app.get("/users/<int:user_id>")
def get_user_id(user_id):
    check_session()

    user = User.query.get_or_404(user_id)
    user_dict = {
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "age": user.age,
    }
    return jsonify(user_dict)


@app.route('/books', methods=['POST', 'GET'])
def handle_books():
    if request.method == 'POST':
        if request.content_type == 'application/json':
            data = request.json
        elif request.content_type == 'application/x-www-form-urlencoded':
            data = request.form
        else:
            return jsonify({'error': 'Invalid content type'}), 400

        book = Book(title=data.get('title'), author=data.get('author'), year=data.get('year'), price=data.get('price'))

        db.session.add(book)
        db.session.commit()

        return jsonify({'message': 'Book created successfully'}), 201
    elif request.method == 'GET':
        args = request.args.get("size")
        if not args:
            books = Book.query.all()
        else:
            books = Book.query.limit(int(args)).all()

        return render_template('books.html', books=books), 200


@app.get("/books/<int:book_id>")
def get_book_id(book_id):
    check_session()

    book = Book.query.get_or_404(book_id)
    return render_template("book_id.html", book=book), 200


@app.route('/purchases', methods=['POST', 'GET'])
def handle_purchases():
    if request.method == 'POST':
        if request.content_type == 'application/json':
            data = request.json
        elif request.content_type == 'application/x-www-form-urlencoded':
            data = request.form
        else:
            return jsonify({'error': 'Invalid content type'}), 400

        user_id = data.get('user_id')
        book_id = data.get('book_id')

        user = User.query.get(user_id)
        book = Book.query.get(book_id)

        if not user or not book:
            return jsonify({'error': 'User or book not found'}), 404

        purchase = Purchase(user=user, book=book)

        db.session.add(purchase)
        db.session.commit()

        return jsonify({'message': 'Purchase created successfully'}), 201
    elif request.method == 'GET':
        args = request.args.get("size")
        if not args:
            purchases = (
                db.session.query(Purchase)
                .join(Book)
                .join(User)
                .filter(Purchase.book_id == Book.id, Purchase.user_id == User.id)
                .all()
            )
        else:
            purchases = (
                db.session.query(Purchase)
                .join(Book)
                .join(User)
                .filter(Purchase.book_id == Book.id, Purchase.user_id == User.id)
                .limit(int(args))
                .all()
            )

        purchase_list = []
        for purchase in purchases:
            purchase_dict = {
                "id": purchase.id,
                "user_id": purchase.user_id,
                "book_id": purchase.book_id,
                "date": purchase.date,
                "title": purchase.book.title,
                "first_name": purchase.user.first_name,
                "last_name": purchase.user.last_name,
            }
            purchase_list.append(purchase_dict)

        return jsonify(purchase_list)


@app.get("/purchases/<int:purchase_id>")
def get_purchase_id(purchase_id):
    check_session()

    purchase = (
        db.session.query(Purchase)
        .join(Book)
        .join(User)
        .filter(
            Purchase.id == purchase_id,
            Purchase.book_id == Book.id,
            Purchase.user_id == User.id,
        )
        .first_or_404()
    )

    purchase_dict = {
        "id": purchase.id,
        "user_id": purchase.user_id,
        "book_id": purchase.book_id,
        "date": purchase.date,
        "title": purchase.book.title,
        "first_name": purchase.user.first_name,
        "last_name": purchase.user.last_name,
    }
    return jsonify(purchase_dict)


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
