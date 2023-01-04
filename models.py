from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Books(db.Model):
    __tablename__ = 'books'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    release_date = db.Column(db.Date, nullable = False)
    num_pages = db.Column(db.Integer, nullable = False)
    cost = db.Column(db.Float, nullable = False)

class Authors(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String, nullable = False)
    middle_name = db.Column(db.String)
    last_name = db.Column(db.String, nullable = False)
    birth_date = db.Column(db.Date, nullable = False)
    death_date = db.Column(db.Date)
    nationality = db.Column(db.String, nullable = False)

class Translator(db.Model):
    __tablename__ = 'translators'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    language = db.Column(db.String, nullable=False)

class Publisher(db.Model):
    __tablename__ = 'publishers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)

class Genre(db.Model):
    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

class Customer(db.Model):
    __tablename__ = 'customer'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)

class Bookgenre(db.Model):
    __tablename__ = 'book_genre'

    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), primary_key=True)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'), primary_key=True)

class Authorbook(db.Model):
    __tablename__ = 'author_book'

    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), primary_key=True)

class Bookpublisher(db.Model):
    __tablename__ = 'book_publisher'

    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), primary_key=True)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publishers.id'), primary_key=True)

class Booktranslator(db.Model):
    __tablename__ = 'book_translator'

    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), primary_key=True)
    translator_id = db.Column(db.Integer, db.ForeignKey('translators.id'), primary_key=True)

class Customerbook(db.Model):
    __tablename__ = 'customer_book'

    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), primary_key=True)
    
