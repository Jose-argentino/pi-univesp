from obj_candidato import Candidato
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase

class InformacoesExtras(DeclarativeBase):
    id_cand = Column(Integer, ForeignKey(Candidato.id_candidato), nullable=False)
    id_info = Column(Integer, primary_key=True)
    certificacao = Column(String(200), nullable=True)
    exp_ferramentas = Column(String(200), nullable=True)
    mensagem = Column(String(200), nullable=True)