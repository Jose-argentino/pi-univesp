
from flask import Flask, render_template, request, redirect, url_for
from entities.candidato import Candidato
from database import SessionLocal, engine, Base  # ajuste o caminho do seu database.py

Base.metadata.create_all(bind=engine)  # cria as tabelas

app = Flask(__name__)

@app.route("/trabalhe", methods=["GET", "POST"])
def trabalhepage():
    if request.method == "POST":
        db = SessionLocal()

        nome = request.form.get("nome")
        telefone = request.form.get("telefone")
        cidade = request.form.get("cidade")
        bairro = request.form.get("bairro")
        nascimento = request.form.get("nascimento")
        experiencia = request.form.get("experiencia")
        cnh = request.form.get("cnh")
        viajar = request.form.get("viajar")
        horas = request.form.get("horas")
        sabado = request.form.get("sabado")
        clt = request.form.get("clt")
        cursos = request.form.get("cursos")
        ferramentas = request.form.get("feramentas")
        mensagem = request.form.get("mensagem")

        habilidades_list = request.form.getlist("habilidades[]")
        habilidades = ",".join(habilidades_list)

        novo_candidato = Candidato(
            nome=nome,
            telefone=telefone,
            cidade=cidade,
            bairro=bairro,
            nascimento=nascimento,
            experiencia=experiencia,
            cnh=cnh,
            viajar=viajar,
            horas=horas,
            sabado=sabado,
            clt=clt,
            cursos=cursos,
            ferramentas=ferramentas,
            mensagem=mensagem,
            habilidades=habilidades
        )

        db.add(novo_candidato)
        db.commit()
        db.close()

        return redirect(url_for('sucesso'))  # você pode redirecionar para uma página de sucesso

    return render_template("trabalhe.html")


@app.route("/candidatos")
def listar_candidatos():
    db = SessionLocal()
    candidatos = db.query(Candidato).all()
    db.close()
    return render_template("candidatos.html", candidatos=candidatos)


@app.route("/sucesso")
def sucesso():
    return "<h1>Cadastro realizado com sucesso!</h1><a href='/'>Voltar</a>"
