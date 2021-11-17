import json

from flask import Flask, jsonify, request

app = Flask(name)

list_of_books = {
    "1": {"author": "Frank Herbert", "title": "Dune", "year": "1965"},
    "2": {"author": "J.R.R. Tolkien", "title": "The Lord of the Rings", "year": "1954"},
    "3": {"author": "J.R.R. Tolkien", "title": "The Hobbit", "year": "1937"},
    "4": {"author": "J.R.R. Tolkien", "title": "The Fellowship of the Ring", "year": "1954"},
    "5": {"author": "J.R.R. Tolkien", "title": "The Two Towers", "year": "1954"},
    "6": {"author": "J.R.R. Tolkien", "title": "The Return of the King", "year": "1955"},
    "7": {"author": "J.R.R. Tolkien", "title": "The Silmarillion", "year": "1954"},
    "8": {"author": "J.R.R. Tolkien", "title": "The Hobbit: An Unexpected Journey", "year": "1939"},
    "9": {"author": "J.R.R. Tolkien", "title": "The Hobbit: The Desolation of Smaug", "year": "1954"},
    "10": {"author": "J.R.R. Tolkien", "title": "The Hobbit: The Battle of the Five Armies", "year": "1954"},
}


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/books", methods=["GET"])
def get_list_of_books():
    return json.dumps(list_of_books)


@app.route("/book/", methods=["GET"])
def get_a_book():
    id = request.args.get('id')
    return jsonify(list_of_books[id])


@app.route("/book/add", methods=["POST"])
def add_book():
    title = request.args.get('title')
    author = request.args.get('author')
    year = request.args.get('year')
    id = len(list_of_books) + 1
    list_of_books[id] = {"title": str(title), "author": str(author), "year": str(year)}
    return list_of_books[id]


@app.route("/book/delete", methods=["DELETE"])
def delete_book():
    delete_book_id = request.args.get('id')
    del list_of_books[delete_book_id]
    return "Book with Id " + delete_book_id + " is deleted"


if name == "main":
    app.run(host='127.0.0.1')