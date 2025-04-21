import config
import mysql.connector #precisa instalar no terminal 'pip install mysql-connector-python'

#Faz primeira conexao para criar banco de dados caso este nao exista
mydb = mysql.connector.connect(host=config.DB_HOST, user=config.DB_USER, password=config.DB_PWD) #mydb é o conector
with mydb.cursor() as cursor:
    cursor.execute(f'CREATE DATABASE IF NOT EXISTS {config.DB_NAME}')
mydb.close()

#Reabre conexao ja com o banco de dados criado
mydb = mysql.connector.connect(host=config.DB_HOST, user=config.DB_USER, password=config.DB_PWD, database=config.DB_NAME)
schema = open('sql/schema.sql', 'r')
values = open('sql/init_values.sql', 'r', encoding="utf8")

with mydb.cursor() as cursor:
    cursor.execute(schema.read(), multi=True)
    while mydb.next_result():
        continue
    cursor.execute(values.read(), multi=True)
    while mydb.next_result():
        continue

mydb.commit()
mydb.close()

schema.close()
values.close()

