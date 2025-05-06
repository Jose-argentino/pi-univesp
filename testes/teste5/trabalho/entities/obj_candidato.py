from sqlalchemy import Column, Integer, String, Date, Boolean
from database import Base  # ou de onde você importa o Base

class Candidato(Base):
    __tablename__ = 'candidatos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    telefone = Column(String(20))
    cidade = Column(String(50), nullable=False)
    bairro = Column(String(50), nullable=False)
    nascimento = Column(Date, nullable=False)
    experiencia = Column(Date, nullable=False)
    cnh = Column(String(10), nullable=False)
    viajar = Column(String(5), nullable=False)
    horas = Column(String(5))
    sabado = Column(String(5))
    clt = Column(String(10))
    cursos = Column(String(500))
    ferramentas = Column(String(500))
    mensagem = Column(String(500))
    # habilidades será uma string com as habilidades separadas por vírgula
    habilidades = Column(String(500))
