from flask import Flask, render_template, redirect, url_for
from models import *
import tables

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:postgres@localhost:5432'
db.init_app(app)

@app.route('/')
def home():
    return redirect('/books')

@app.route('/<tabulka>', methods=['GET'])
def database(tabulka):
    tables_list = tables.get()
    table = tables_list.get(tabulka)
    result = table.query.all()
    columns = []
    for i in tables_list.get(tabulka).__table__.columns:
        i = str(i)
        columns.append(i.split('.')[-1])
    return render_template('tables.html', result = result, columns = columns, tabulka = tabulka, tables_list = tables_list)



if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")