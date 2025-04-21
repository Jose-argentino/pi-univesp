from entities.obj_candidato import Candidato
from sqlalchemy import Column, Integer, String, ForeignKey
from entities.base import Base
from sqlalchemy.orm import relationship

class InformacoesExtras(Base):
    __tablename__= "informacoes_extras"

    id_cand = Column(Integer, ForeignKey(Candidato.id_candidato), nullable=False)
    id_info = Column(Integer, primary_key=True)
    certificacao = Column(String(200), nullable=True)
    exp_ferramentas = Column(String(200), nullable=True)
    mensagem = Column(String(200), nullable=True)

