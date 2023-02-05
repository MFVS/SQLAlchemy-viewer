from flask import Flask, render_template, redirect, url_for, session, request
import models
import tables

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432"
app.secret_key = b'_5#y2L"F4Q8z\n\xeffc]/'
with app.app_context():
    models.db.init_app(app)
    models.db.create_all()
    models.db.session.commit()


@app.before_request
def make_session_permanent():
    session.permanent = True
    if not "url" in session:
        session["url"] = "/"

@app.after_request
def store_last_url(response):
    # print("WEREEEEEE")
    # if request.method != "POST":
    #     print("Whhattt")
    #     return True
    print(request.url)
    session["url"] = request.base_url
    print("session url:", session.get("url"))
    return response

@app.route('/<tabulka>', methods=['GET'])
def table_view(tabulka):
    tables_list = tables.get()
    table = tables_list.get(tabulka)
    result = table.query.all()
    columns = []
    for i in tables_list.get(tabulka).__table__.columns:
        i = str(i)
        columns.append(i.split('.')[-1])
    return render_template('tables.html', result = result, columns = columns, tabulka = tabulka, tables_list = tables_list)

@app.route("/")
def home():
    table_to_get = list(tables.get())[0] or 'not_found'
    return redirect(str(table_to_get))

@app.route("/favicon.ico")
def icon():
    return app.send_static_file("book.ico")

@app.route("/insert", methods=["POST"])
def insert_something():
    print("trying to insert!")
    with app.app_context():
        e = models.db.engine
    return ("", 204)


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")