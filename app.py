from flask import Flask
app = Flask(__name__)

@app.route("/")
def start():
    return """
<!doctype html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Чернухина Полина Валерьевна, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h>web-сервер на flask</h>

        <footer>
            &copy; Чернухина Полина, ФБИ-23, 3 курс, 2024
        </footer>
    </body>
</html>
"""