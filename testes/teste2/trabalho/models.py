from trabalho import db
from entities.obj_candidato import Candidato
from entities.obj_contratacao import Contratacao
from entities.obj_habilidade import Habilidade
from entities.obj_habilidades_candidato import HabilidadesCandidato
from entities.obj_informacoes_extras import InformacoesExtras

# Aqui apenas importamos os modelos para que o Flask-Migrate ou db.create_all() saiba deles
# Não precisa colocar nada mais aqui a princípio
