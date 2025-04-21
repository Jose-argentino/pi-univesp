
from obj_contratacao import Contratacao
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import DeclarativeBase

class Candidato(DeclarativeBase):
    id_candidato = Column(Integer, primary_key=True)
    p_nome = Column(String(45), nullable=False)
    sobrenome = Column(String(45), nullable=False)
    bairro = Column(String(45), nullable=True)
    cidade = Column(String(45), nullable=False)
    dt_nasc = Column(DateTime, nullable=True)
    telefone = Column(String(13), nullable=False)
    exp_anos = Column(Integer, nullable=False)
    cnh = Column(String(5), nullable=True)
    hora_extra = Column(Boolean, nullable=True)
    trab_sabado = Column(Boolean, nullable=True)
    viagem_trab = Column(Boolean, nullable=True)
    id_contr = Column(Integer(), ForeignKey(Contratacao.id_contrato))
