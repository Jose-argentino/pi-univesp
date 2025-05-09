from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from entities.base import Base

class Contratacao(Base):
    __tablename__ = "contratacao"

    id_contrato = Column(Integer, primary_key=True)
    tipo_contrato = Column(String(45), nullable=False)
    #candidato = relationship('Candidato', backref='contrato')
