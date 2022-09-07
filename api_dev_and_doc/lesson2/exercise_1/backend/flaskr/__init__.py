from crypt import methods
import os
from turtle import title
from urllib import response
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Book
BOOKS_PER_SHELF = 8

def paginate_books(request, selection):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * BOOKS_PER_SHELF
    end = start + BOOKS_PER_SHELF
    books = [book.format() for book in selection]
    current_books = books[start:end]
    return current_books

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    #CORS Headers
    @app.after_request
    def after_request(request):
        response.headers.add("Access-Control-Allow-Headers", "Content_type, Authorizations, True")
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
        )
        return response

    @app.route("/books")
    def retrive_books():
        books = Book.query.all()
        current_books = paginate_books(request=books)
        if len(current_books) == 0:
            abort(404)

        return jsonify({
            "success": True,
            "books": current_books,
            "total_books": len(books),
        })

    @app.route("/books/<int:book_id>", methods=["PATCH"])
    def update_book(book_id):
        body = request.get_json()

        try:
            book = Book.query.filter(Book.id).first()
            if book is None:
                abort(404)
            if "rating" in body:
                book.rating = int(body.get("rating"))
            book.update()
            
            return jsonify({
                "success": True,
                "id": book.id,
            })
        except:
            abort(400)

    @app.route("/books/<int:book_id")
    def delete_book(book_id):
        try:
            book = Book.query.filter(Book.id == book_id).first()

            if len(book) == 0:
                abort(404)
            book.delete()
            book_list = Book.query.all()
            current_books = paginate_books(request, book_list)

            return jsonify({
                "success": True,
                "deleted": book_id,
                "books": current_books,
                "total_books": len(Book.query.all()),
            })
        except:
            abort(422)

    @app.route("/books", methods=["POST"])
    def create_book():
        body = request.get_json()

        book_title = body.get("title", None)
        author_name = body.get("author", None)
        book_rating = body.get("rating", None)

        try:
            book = Book(book_title, author_name, book_rating)

            # save the book data in the db
            book.insert()

            books_list = Book.query.all()
            current_books = paginate_books(request, books_list)
            return jsonify({
                "success": True,
                "created": book.id,
                "books": current_books,
                "total_bookss": len(Book.query.all()),
            })
        except:
            abort(422)

    return app