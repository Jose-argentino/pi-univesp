import mysql.connector

# Inicializa a variável conn como None fora do bloco try
conn = None

# Teste a conexão
try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',  # Substitua por seu usuário MySQL, caso seja diferente
        password='senha',  # Substitua pela senha do seu MySQL
        database='bd_jardineiros'  # Substitua pelo nome do seu banco de dados
    )
    print("Conexão com o banco de dados bem-sucedida!")
except mysql.connector.Error as err:
    print(f"Erro: {err}")
finally:
    # Verifica se a conexão foi criada e a fecha corretamente
    if conn and conn.is_connected():
        conn.close()
        print("Conexão fechada.")
