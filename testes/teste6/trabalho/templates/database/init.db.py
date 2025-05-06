import mysql.connector
import config

# Conectando ao MySQL para criar o banco de dados
mydb = mysql.connector.connect(
    host=config.DB_HOST,
    user=config.DB_USER,
    password=config.DB_PWD
)

with mydb.cursor() as cursor:
    # Cria o banco de dados caso não exista
    cursor.execute(f'CREATE DATABASE IF NOT EXISTS {config.DB_NAME}')
mydb.close()

# Reabre a conexão com o banco de dados já criado
mydb = mysql.connector.connect(
    host=config.DB_HOST,
    user=config.DB_USER,
    password=config.DB_PWD,
    database=config.DB_NAME
)

# Abrindo os scripts SQL para criação das tabelas e inserção dos valores
schema = open('sql/schema.sql', 'r')
values = open('sql/init_values.sql', 'r', encoding="utf8")
exemplo = open('sql/mock.sql', 'r', encoding="utf8")

# Executando os comandos SQL
with mydb.cursor() as cursor:
    cursor.execute(schema.read(), multi=True)
    while mydb.next_result():
        continue
    cursor.execute(values.read(), multi=True)
    while mydb.next_result():
        continue
    cursor.execute(exemplo.read(), multi=True)
    while mydb.next_result():
        continue

mydb.commit()  # Confirma as alterações no banco de dados
mydb.close()  # Fecha a conexão com o banco

# Fechando os arquivos
schema.close()
values.close()
exemplo.close()
