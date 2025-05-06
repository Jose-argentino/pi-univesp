# Importando as bibliotecas necessárias
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Criando uma instância da aplicação Flask
app = Flask(__name__)

# Configurando o banco de dados SQLite (o arquivo será 'usuarios.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
# Desativando o rastreamento de modificações (não necessário e economiza recurso)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Criando a instância do SQLAlchemy, passando a app
db = SQLAlchemy(app)

# Definindo o modelo da tabela 'usuario' no banco de dados
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Campo ID, chave primária
    nome = db.Column(db.String(100), nullable=False)  # Campo nome, obrigatório
    email = db.Column(db.String(100), nullable=False)  # Campo email, obrigatório

    def __repr__(self):
        return f'<Usuario {self.nome}>'  # Representação do objeto quando impresso

# Rota para o formulário de cadastro de usuário
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        # Se o formulário foi enviado, pegamos os dados enviados
        nome = request.form['nome']
        email = request.form['email']

        # Criamos uma nova instância do usuário com os dados recebidos
        novo_usuario = Usuario(nome=nome, email=email)

        # Adicionamos o novo usuário no banco de dados
        db.session.add(novo_usuario)
        db.session.commit()

        # Após salvar, redirecionamos para a página de lista de usuários
        return redirect(url_for('usuarios'))
    
    # Se for GET (primeiro acesso), apenas renderiza o formulário
    return render_template('cadastro.html')

# Rota para exibir todos os usuários cadastrados
@app.route('/usuarios')
def usuarios():
    # Busca todos os usuários no banco de dados
    lista_usuarios = Usuario.query.all()
    
    # Passa a lista de usuários para o template 'usuarios.html'
    return render_template('usuarios.html', usuarios=lista_usuarios)

# Inicializa o banco e roda o servidor
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco, caso não existam
    app.run(debug=True)  # Inicia o servidor Flask com modo debug
