import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:senha@localhost/nome_do_banco'  # Altere os dados da sua conexão
    SQLALCHEMY_TRACK_MODIFICATIONS = False
