from sqlalchemy import Column, Integer, String
from entities.base import Base

class Habilidade(Base):
    __tablename__= "habilidade"

    id_hab = Column(Integer, primary_key=True)
    hab_nome = Column(String(200), nullable=False)