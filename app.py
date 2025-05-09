from flask import Flask, render_template, request, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from entities.obj_contratacao import Contratacao
from entities.obj_candidato import Candidato
from entities.obj_habilidade import Habilidade
from entities.obj_habilidades_candidato import HabilidadesCandidato
from entities.obj_informacoes_extras import InformacoesExtras
import database.config as config

app = Flask('__name__')
app.config[
    "SQLALCHEMY_DATABASE_URI"] = f'mysql+pymysql://{config.DB_USER}:{config.DB_PWD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}'
db = SQLAlchemy(app)


@app.route('/prestadores')
def cadastrados():
    # Select que retorna algumas informações mais relevantes sobre o candidato
    result1 = db.session.query(Candidato, Contratacao, InformacoesExtras).join(Contratacao).join(
        InformacoesExtras).all()

    # Select que retorna o nome do candidato e as suas habilidades
    # result2 = db.session.query(HabilidadesCandidato, Candidato, Habilidade).join(Candidato).join(Habilidade).all()
    # for i in result2:
    # print(i[1].p_nome, i[2].hab_nome)

    return render_template('admin.html', cadastrobasico=result1)


@app.route('/')
def servico():
    return render_template('servico.html')


@app.route('/cadastro', methods=('GET', 'POST'))
def cadastro():
    if request.method == 'POST':
        novo_candidato = Candidato(
            p_nome=request.form['nome'],
            sobrenome='',
            bairro=request.form['bairro'],
            cidade=request.form['cidade'],
            dt_nasc=request.form['nascimento'],
            telefone=request.form['telefone'],
            exp_anos=request.form['experiencia'],
            hora_extra=request.form['horas'] == 'sim',
            trab_sabado=request.form['sabado'] == 'sim',
            cnh=request.form['cnh'],
            viagem_trab=request.form['viajar'] == 'sim',
            id_contr=request.form['clt']
        )

        cand_informacoes = InformacoesExtras(
            candidato=novo_candidato,
            certificacao=request.form['cursos'],
            exp_ferramentas=request.form['ferramentas'],
            mensagem=request.form['mensagem']
        )

        cand_habilidades = HabilidadesCandidato(
            candidato=novo_candidato,
            id_hab=5
        )

        # if not title:
        #     flash('O título é obrigatório!')
        # else:

        db.session.add(novo_candidato)
        db.session.add(cand_informacoes)
        db.session.add(cand_habilidades)
        db.session.commit()
        # return redirect(url_for('index'))
    return render_template('trabalhe.html')


if __name__ == '__main__':
    app.run(debug=True)
