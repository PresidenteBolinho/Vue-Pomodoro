from flask import Flask, render_template

#configuração da aplicação
DEBUG = True


app = Flask(__name__)

#Rota raiz
@app.route('/')
def index():
    return render_template('index.html')


#Login e registro
@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/registro')
def registro():
    return render_template('registro.html')


#Aplicação Pomodoro
@app.route('/pomodoro')
def pomodoro():
    return render_template('pomodoro.html')


if __name__ == '__main__':
    app.run()
