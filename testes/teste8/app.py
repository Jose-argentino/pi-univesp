from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configurações do banco de dados MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://usuario:senha@localhost/trabalhe_conosco'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o SQLAlchemy
db = SQLAlchemy(app)

# Modelo de dados para o candidato
class Candidato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20))
    cidade = db.Column(db.String(50), nullable=False)
    bairro = db.Column(db.String(50), nullable=False)
    nascimento = db.Column(db.Date, nullable=False)
    experiencia = db.Column(db.Date, nullable=False)
    cnh = db.Column(db.String(10), nullable=False)
    viajar = db.Column(db.String(3), nullable=False)
    habilidades = db.Column(db.Text)
    horas = db.Column(db.String(3))
    sabado = db.Column(db.String(3))
    clt = db.Column(db.String(10))
    cursos = db.Column(db.Text)
    ferramentas = db.Column(db.Text)
    mensagem = db.Column(db.Text)

    def __repr__(self):
        return f'<Candidato {self.nome}>'

# Rota para exibir o formulário
@app.route('/trabalhe', methods=['GET'])
def trabalhe():
    return render_template('trabalhe.html')

# Rota para processar o formulário
@app.route('/trabalhe', methods=['POST'])
def enviar():
    nome = request.form['nome']
    telefone = request.form.get('telefone')
    cidade = request.form['cidade']
    bairro = request.form['bairro']
    nascimento = request.form['nascimento']
    experiencia = request.form['experiencia']
    cnh = request.form['cnh']
    viajar = request.form['viajar']
    habilidades = request.form.getlist('habilidades[]')
    horas = request.form.get('horas')
    sabado = request.form.get('sabado')
    clt = request.form.get('clt')
    cursos = request.form.get('cursos')
    ferramentas = request.form.get('ferramentas')
    mensagem = request.form.get('mensagem')

    novo_candidato = Candidato(
        nome=nome,
        telefone=telefone,
        cidade=cidade,
        bairro=bairro,
        nascimento=nascimento,
        experiencia=experiencia,
        cnh=cnh,
        viajar=viajar,
        habilidades=','.join(habilidades),
        horas=horas,
        sabado=sabado,
        clt=clt,
        cursos=cursos,
        ferramentas=ferramentas,
        mensagem=mensagem
    )

    db.session.add(novo_candidato)
    db.session.commit()

    return redirect(url_for('candidatos'))

# Rota para listar os candidatos cadastrados
@app.route('/candidatos')
def candidatos():
    todos_candidatos = Candidato.query.all()
    return render_template('candidatos.html', candidatos=todos_candidatos)

if __name__ == '__main__':
    # Cria as tabelas no banco de dados
    with app.app_context():
        db.create_all()
    app.run(debug=True)
