from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from entities.obj_contratacao import Contratacao
from entities.obj_candidato import Candidato
from entities.obj_habilidade import Habilidade
from entities.obj_habilidades_candidato import HabilidadesCandidato
from entities.obj_informacoes_extras import InformacoesExtras
import database.config as config

app = Flask('__name__')
app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql+pymysql://{config.DB_USER}:{config.DB_PWD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}'
db = SQLAlchemy(app)

@app.route('/prestadores')
def cadastrados():
    #Select que retorna algumas informações mais relevantes sobre o candidato
    result1 = db.session.query(Candidato, Contratacao, InformacoesExtras).join(Contratacao).join(InformacoesExtras).all()
    for i in result1: #0 se refere a candidato, 1 a contratação e 2 a informações extras
        print(i[0].p_nome+' '+i[0].sobrenome, i[0].cidade, i[0].telefone, i[0].exp_anos, i[0].hora_extra, i[1].tipo_contrato, i[2].certificacao)

    #Select que retorna o nome do candidato e as suas habilidades
    #result2 = db.session.query(HabilidadesCandidato, Candidato, Habilidade).join(Candidato).join(Habilidade).all()
    #for i in result2:
        #print(i[1].p_nome, i[2].hab_nome)

    return render_template('admin.html', cadastrobasico = result1)

@app.route('/')
def cadastro():
    return render_template('trabalhe.html')

if __name__ == '__main__':
    app.run(debug=True)