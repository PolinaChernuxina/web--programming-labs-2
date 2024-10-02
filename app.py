from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
    return """
<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>
        
        <div>
            <ol>
                <li>
                    <a href="/lab1">Лабораторная работа 1</a>
                </li>
            
            </ol>
        </div>

        <footer>
            &copy; Чернухина Полина, ФБИ-23, 3 курс, 2024 
        </footer>
    </body>
</html>
"""

@app.route("/lab1")
def lab1():
    return """
<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>НГТУ, ФБ, Лабораторная работа 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>
        <p>Flask — фреймворк для создания веб-приложений на языке программирования Python, 
        использующий набор инструментов Werkzeug, а также шаблонизатор Jinja2. Относится к 
        категории так называемых микрофреймворков — минималистичных каркасов веб-приложений, 
        сознательно предоставляющих лишь самые базовые возможности.</p>
        
        <a href="/menu">Меню</a>
        
        <h2>Реализованные роуты</h2>
        <div>
            <ol>
                <li>
                    <a href="lab1/oak">Дуб</a>
                </li>
                <li>
                    <a href="lab1/student">Студент</a>
                </li>
                <li>
                    <a href="lab1/python">Python</a>
                </li>
                <li>
                    <a href="lab1/mfg">Мир йоги</a>
                </li>
            
            </ol>
        </div>
        <footer>
            &copy; Чернухина Полина, ФБИ-23, 3 курс, 2024 
        </footer>
    </body>
</html>
"""
@app.route("/lab1/oak")
def oak():
    return '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <title>Дуб</title>
</head>
    <body>
        <h1>Дуб</h1>
        <img src="''' + url_for('static', filename='oak.jpg') + '''">
    </body>
</html>
'''

@app.route("/lab1/student")
def student():
    return '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
    <title>Студент</title>
</head>
<body>
    <h1>Чернухина Полина Валерьевна</h1>
    <img src="''' + url_for('static', filename='logo.png') + '''" alt="Логотип НГТУ">
</body>
</html>
'''

@app.route("/lab1/python")
def python_info():
    return '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
    <title>Python</title>
</head>
<body>
    <h1>Язык программирования Python</h1>
    <p>Python — это язык программирования, который широко используется в интернет-приложениях, 
    разработке программного обеспечения, науке о данных и машинном обучении (ML). Разработчики 
    используют Python, потому что он эффективен, прост в изучении и работает на разных платформах.</p>
    
    <p>Веб-разработка на стороне сервера включает в себя сложные серверные функции, с помощью которых веб-сайты отображают информацию для пользователя. Например, веб-сайты должны 
    взаимодействовать с базами данных и другими веб-сайтами, а также защищать данные при их отправке по сети. </p>
    <img src="''' + url_for('static', filename='python.jpg') + '''" alt="Программирование на Python">
</body>
</html>
'''

@app.route("/lab1/mfg")
def mfg():
    return '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <style>
            body {
                background-color: #ADD8E6;
            }
            h1 {
                font-weight: bold;
            }
    </style>
    <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
    <title>Мир йоги</title>
</head>
<body>
    <h1>Мир йоги</h1>
    <p><b>Йога</b> — не просто фитнес, а комплекс физических упражнений, дыхательных техник и практик концентрации внимания. Это целая философия, древнее учение, а для многих — образ жизни. Йога развивает человека всесторонне — через тело, ум и эмоции, а также помогает достичь гармонии физического и психологического состояния. 
    Систематические занятия благотворно влияют на все органы и системы, позволяют достичь душевного равновесия.</p>
    
    <p2>Одна из главных причин, почему йога полезна, кроется в особенности организма человека. — <i>
    асимметричность дыхания</i>. Ученые доказали, что каждые 2,5 часа дыхание переключается с одной ноздри на другую. В хатха-йоге, ставшей наиболее популярным направлением йоги, уделяют внимание такой особенности. Для этого используются дыхательные практики с асимметричным 
    дыханием: левой ноздрей для придания тонуса и бодрости, а затем правой, наоборот, для расслабления.</p2>
    <img src="''' + url_for('static', filename='йога2.jpg') + '''" alt="Программирование на Python">
</body>
</html>
'''

@app.route('/lab2/example')
def example():
    name = 'Полина Чернухина'
    course = '3 курс'
    lab = 'Лабораторная работа 2'
    group = 'ФБИ-23'
    return render_template('example.html', name=name, course=course, lab=lab, group=group)
    