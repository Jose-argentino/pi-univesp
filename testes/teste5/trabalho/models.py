from flask_sqlalchemy import SQLAlchemy

# Inicializando o SQLAlchemy
db = SQLAlchemy()

# Modelo para mapear a tabela 'candidatos' no banco de dados
class Candidato(db.Model):
    __tablename__ = 'candidatos'  # Nome da tabela no banco de dados

    # Definindo as colunas da tabela
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    telefone = db.Column(db.String(20))
    cidade = db.Column(db.String(100))
    bairro = db.Column(db.String(100))
    data_nascimento = db.Column(db.Date)
    experiencia_ano = db.Column(db.Integer)
    cnh = db.Column(db.String(10))
    habilidades = db.Column(db.String(255))
    hora_extra = db.Column(db.String(10))
    sabado = db.Column(db.String(10))
    tipo_contrato = db.Column(db.String(10))
    cursos = db.Column(db.String(255))
    ferramentas = db.Column(db.String(255))
    mensagem = db.Column(db.Text)

    # Inicializador do modelo
    def __init__(self, nome, telefone, cidade, bairro, data_nascimento, experiencia_ano, cnh, habilidades, hora_extra, sabado, tipo_contrato, cursos, ferramentas, mensagem):
        self.nome = nome
        self.telefone = telefone
        self.cidade = cidade
        self.bairro = bairro
        self.data_nascimento = data_nascimento
        self.experiencia_ano = experiencia_ano
        self.cnh = cnh
        self.habilidades = habilidades
        self.hora_extra = hora_extra
        self.sabado = sabado
        self.tipo_contrato = tipo_contrato
        self.cursos = cursos
        self.ferramentas = ferramentas
        self.mensagem = mensagem
