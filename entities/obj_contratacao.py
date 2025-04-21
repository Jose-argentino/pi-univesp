from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

class Contratacao(DeclarativeBase):
    id_contrato = Column(Integer, primary_key=True)
    tipo_contrato = Column(String(45), nullable=False)