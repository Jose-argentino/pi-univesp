from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo da tabela
class Candidato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    mensagem = db.Column(db.Text)

# Criar o banco de dados
with app.app_context():
    db.create_all()

# Rota para o formulário
@app.route("/trabalhe", methods=["GET", "POST"])
def trabalhe():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        mensagem = request.form["mensagem"]

        novo_candidato = Candidato(nome=nome, email=email, mensagem=mensagem)
        db.session.add(novo_candidato)
        db.session.commit()

        return redirect("/admin")
    return render_template("trabalhe.html")

# Rota para exibir os dados
@app.route("/admin")
def admin():
    candidatos = Candidato.query.all()
    return render_template("admin.html", candidatos=candidatos)

if __name__ == "__main__":
    app.run(debug=True)
