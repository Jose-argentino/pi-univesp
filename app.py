from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from entities.obj_contratacao import Contratacao
import database.config as config


app = Flask('__name__')
app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql+pymysql://{config.DB_USER}:{config.DB_PWD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}'
db = SQLAlchemy(app)

x = Contratacao.query.all()
print("aquiii", x)