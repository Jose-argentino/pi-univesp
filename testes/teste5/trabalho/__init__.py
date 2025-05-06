from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Configuração do banco de dados
# Usando mysql-connector
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:senha@localhost/bd_jardineiros'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialização do banco de dados e migrações
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Importa as rotas após a configuração
from trabalho.views import index
