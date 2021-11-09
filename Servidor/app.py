from flask import Flask, render_template

#configuração da aplicação
DEBUG = True


app = Flask(__name__)

#Rota raiz
@app.route('/')
def index():
    return "<h1>Index</h1>"


#Login e registro
@app.route('/login')
def login():
    return "<h1>Login</h1>"


@app.route('/registro')
def registro():
    return "<h1>Registro</h1>"


#Aplicação Pomodoro
@app.route('/pomodoro')
def pomodoro():
    return "<h1>Pomodoro</h1>"


if __name__ == '__main__':
    app.run()
