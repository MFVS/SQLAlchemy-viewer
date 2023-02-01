from flask import Flask, render_template, redirect, url_for
import models
import tables

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:postgres@localhost:5432'

with app.app_context():
    models.db.init_app(app)
    models.db.create_all()
    models.db.session.commit()

@app.route('/favicon.ico')
def icon():
    # return redirect('https://www.google.com/favicon.ico')
    print('WEEEEEE')
    return app.send_static_file('book.ico')

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