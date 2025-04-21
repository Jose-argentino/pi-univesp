import databaseConfig as dc
import mysql.connector #precisa instalar no terminal 'pip install mysql-connector-python'

#Faz primeira conexao para criar banco de dados caso este nao exista
mydb = mysql.connector.connect(host=dc.DB_HOST, user=dc.DB_USER, password=dc.DB_PWD) #mydb é o conector
cursor = mydb.cursor()
cursor.execute(f'CREATE DATABASE IF NOT EXISTS {dc.DB_NAME}')
mydb.close()

#Reabre conexao ja com o banco de dados criado
mydb = mysql.connector.connect(host=dc.DB_HOST, user=dc.DB_USER, password=dc.DB_PWD, database=dc.DB_NAME)
schema = open('schema.sql', 'r')
values = open('default_values.sql', 'r')

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
