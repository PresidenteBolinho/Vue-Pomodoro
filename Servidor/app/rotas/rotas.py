from app import app
from flask import jsonify, request, redirect
from flask_cors import CORS


CORS(app, resource={r'/*': {'origins': '*'}})


USUARIOS = [
    {
        'primeiro_nome': 'admin',
        'segundo_nome': 'root',
        'usuario': 'admin',
        'email': 'admin@admin.com',
        'senha': 'admin'
    }
]
TAREFAS = []


#Rota raiz
@app.route('/', methods=['GET'])
def index():
    return "<h1>Index</h1>"


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('O servidor está funcionado!')


#Autenticação
@app.route('/login', methods=['POST', 'GET'])
def acesso():
    response_object = {'status': 'success'}

    if request.method == 'POST':
        post_data = request.get_json()
        post_data['usuario'] in USUARIOS

    return jsonify(response_object)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    response_object = {'status': 'success'}

    if request.method == 'POST':
        post_data = request.get_json()
        USUARIOS.append({
            'primeiro_nome': post_data.get('primeiro_nome'),
            'segundo_nome': post_data.get('segundo_nome'),
            'usuario': post_data.get('usuario'),
            'email': post_data.get('email'),
            'senha': post_data.get('senha')
        })
        response_object['message'] = 'Usuário registrado!'
        return redirect('http://localhost:8080/autenticacao')
    else:
        response_object['usuarios'] = USUARIOS

    return jsonify(response_object)
