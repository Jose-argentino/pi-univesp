from flask import Flask, render_template
from models import db, Candidato  # Importando o banco de dados e o modelo

app = Flask(__name__)

# Configuração do banco de dados MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:senha@localhost/nome_do_banco'  # Altere 'senha' e 'nome_do_banco' para o que for apropriado
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desabilita a notificação de modificações do banco de dados

# Inicializa a conexão com o banco
db.init_app(app)

@app.route('/admin')
def admin():
    # Buscando todos os candidatos do banco de dados
    candidatos = Candidato.query.all()

    # Passando os dados para o template 'admin.html'
    return render_template('admin.html', candidatos=candidatos)

if __name__ == '__main__':
    app.run(debug=True)
