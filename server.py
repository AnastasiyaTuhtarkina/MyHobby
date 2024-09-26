from flask import Flask, render_template, g


app = Flask(__name__)
#настройки приложения
app.secret_key = 'asdf1234'


navMenu = [
    {"link": "/index", "name": "Главная"},
    {"link": "/about", "name": "Обо мне"},
    {"link": "/contacts", "name": "Обратная связь"}
]

@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html", menu=navMenu)


@app.route("/about")
def about():
    return render_template("about.html", menu=navMenu)


@app.route("/contacts")
def contacts():
    return render_template("contacts.html", menu=navMenu)


#разрыв подключения
@app.teardown_appcontext
def close_connect(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()

if __name__ == "__main__":
    app.run()