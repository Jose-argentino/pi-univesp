from obj_candidato import Candidato
from obj_habilidade import Habilidade
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase


class Habilidades_candidato(DeclarativeBase):
    id_candidato = Column(Integer, ForeignKey(Candidato.id_candidato), primary_key=True)
    id_hab = Column(Integer, ForeignKey(Habilidade.id_hab), primary_key=True)
