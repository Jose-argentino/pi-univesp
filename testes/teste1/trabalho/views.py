from trabalho import app
from flask import render_template, url_for
from trabalho import db
from entities.obj_candidato import Candidato

@app.route('/teste_db')
def test_db():
    candidatos = db.session.query(Candidato).all()
    return f"Total de candidatos: {len(candidatos)}"


#rotas para as paginas do navibar

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Principal/')
def indexpage():
    return render_template('index.html')

@app.route('/historia/')
def sobrepage():
    return render_template('sobre.html')

@app.route('/serviço/')
def servicopage():
    return render_template('servico.html')


@app.route('/Contato/')
def contatopage():
    return render_template('contato.html')

@app.route('/Nossa_equipe/')
def trabalhepage():
    return render_template('trabalhe.html')

@app.route('/Candidatos/')
def adminpage():
    #cliamos variaveves 
    usuario = 'josé'
    idade = '19'
    #que são amazenadas em um dicionario
    context = {
        'usuario' : usuario,
        'idade' : idade,
        }
    return render_template('admin.html', context=context)