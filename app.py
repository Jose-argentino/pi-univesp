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
    # Select que retorna algumas informações mais relevantes sobre todos os candidatos
    result1 = db.session.query(Candidato, Contratacao, InformacoesExtras).join(Contratacao).join(
        InformacoesExtras).order_by(Candidato.id_candidato).all()

    return render_template('admin.html', cadastrobasico=result1)


@app.route('/<int:id_candidato>')
def detalhes_cadastrados(id_candidato):
    result1 = (db.session.query(Candidato, Contratacao, InformacoesExtras)
               .join(Contratacao, Contratacao.id_contrato == Candidato.id_contr)
               .join(InformacoesExtras, InformacoesExtras.id_cand == Candidato.id_candidato)
               .filter(Candidato.id_candidato == id_candidato).first())

    result2 = (db.session.query(Habilidade.hab_nome, HabilidadesCandidato, Candidato)
                .join(Candidato, Candidato.id_candidato == HabilidadesCandidato.id_candidato)
                .join(Habilidade, Habilidade.id_hab == HabilidadesCandidato.id_hab)
                .filter(Candidato.id_candidato == id_candidato).all())

    listaHabilidade = list(map(lambda tupla: tupla[0], result2))

    return render_template('detalhes.html', result=result1, result_hab=listaHabilidade)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/servico')
def servico():
    return render_template('contato.html')


@app.route('/cadastro', methods=('GET', 'POST'))
def cadastro():
    if request.method == 'POST':
        novo_candidato = Candidato(
            nome=request.form['nome'],
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
        db.session.add(novo_candidato)

        cand_informacoes = InformacoesExtras(
            candidato_rel=novo_candidato,
            certificacao=request.form['cursos'],
            exp_ferramentas=request.form['ferramentas'],
            mensagem=request.form['mensagem']
        )
        db.session.add(cand_informacoes)

        habilidades = request.form.getlist('habilidades')
        for habilidade in habilidades:
            cand_habilidades = HabilidadesCandidato(
                candidato_rel=novo_candidato,
                id_hab=habilidade
            )
            db.session.add(cand_habilidades)

        db.session.commit()
        return redirect(url_for('cadastrados'))

    return render_template('trabalhe.html')


if __name__ == '__main__':
    app.run(debug=True)
