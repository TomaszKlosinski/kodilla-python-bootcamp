from flask import render_template
from app import app, db
from app.models import Author, Book, Borrow


def init_dummy_data():
    author = Author(name="Eric")
    db.session.add(author)

    book = Book(title="Harry Potter", author_id=author.id)
    db.session.add(book)

    borrow = Borrow(borrower="Tomasz Klosinski", book_id=book.id)
    db.session.add(borrow)

    db.session.commit()


@app.route('/')
def index():
    if Author.query.first() is None:
        init_dummy_data()

    authors = Author.query.all()
    books = Book.query.all()
    borrows = Borrow.query.all()

    return render_template("index.html", authors=authors, books=books, borrows=borrows)