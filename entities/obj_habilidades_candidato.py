from entities.obj_candidato import Candidato
from entities.obj_habilidade import Habilidade
from sqlalchemy import Column, Integer, ForeignKey
from entities.base import Base
from sqlalchemy.orm import relationship

class HabilidadesCandidato(Base):
    __tablename__ = "habilidades_candidato"

    id_candidato = Column(Integer, ForeignKey(Candidato.id_candidato), primary_key=True)
    id_hab = Column(Integer, ForeignKey(Habilidade.id_hab), primary_key=True)

    candidato = relationship('Candidato', backref='cand_habilidade', foreign_keys=[id_candidato])
    habilidade = relationship('Habilidade', backref='hab_habilidade', foreign_keys=[id_hab])



