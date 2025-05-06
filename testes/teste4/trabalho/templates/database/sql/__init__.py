from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config  # Importa o arquivo config.py para pegar as credenciais

app = Flask(__name__)

# Configuração da conexão com o banco MySQL (corrigido)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{config.DB_USER}:{config.DB_PWD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"

# Desativa o aviso de modificações do SQLAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Cria a instância do banco de dados com SQLAlchemy
db = SQLAlchemy(app)

# Adiciona suporte a migrações com Flask-Migrate
migrate = Migrate(app, db)

# Importa as rotas
from trabalho.views import index
