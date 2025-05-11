#!/bin/bash

echo "Instalando dependências no ambiente virtual..."
pip install flask flask_sqlalchemy

echo "Criando banco de dados..."
python3 init.db.py

