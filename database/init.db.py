import mysql.connector
import os

# Configuração da conexão para criar o banco
config_base = {
    'user': 'root',
    'password': '123',  # Troque pela sua senha
    'host': 'localhost'
}

# Configuração da conexão com o banco já criado
config = {
    'user': 'root',
    'password': '123',
    'host': 'localhost',
    'database': 'pi_univesp',
    'raise_on_warnings': True
}

# Caminho base do projeto
base_path = os.path.dirname(os.path.abspath(__file__))

try:
    # Conecta sem banco para criar o banco
    conn = mysql.connector.connect(**config_base)
    cursor = conn.cursor()
    try:
        cursor.execute("CREATE DATABASE pi_univesp;")
        print("Banco de dados 'pi_univesp' criado com sucesso.")
    except mysql.connector.Error as err:
        if err.errno == 1007:
            print("Banco de dados 'pi_univesp' já existe. Continuando...")
        else:
            raise
    finally:
        cursor.close()
        conn.close()
except mysql.connector.Error as err:
    print(f"Erro ao criar banco: {err}")
    exit(1)

try:
    # Conecta ao banco já existente
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    print("Executando: -- Desabilita verificação de chaves estrangeiras temporariamente")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")

    print("Executando: DROP TABLE IF EXISTS...")
    cursor.execute("SHOW TABLES;")
    tabelas = cursor.fetchall()
    for (tabela,) in tabelas:
        cursor.execute(f"DROP TABLE IF EXISTS {tabela};")

    print("Executando: -- Reabilita verificação de chave estrangeira")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")

    print("Executando: -- Criação das tabelas")
    with open(os.path.join(base_path, "sql/schema.sql"), 'r') as f:
        schema_sql = f.read()

    for statement in schema_sql.split(';'):
        stmt = statement.strip()
        if stmt:
            cursor.execute(stmt + ';')

    print("Executando: -- Inserção de dados de exemplo (se existir)")
    dados_path = os.path.join(base_path, "sql/dados_exemplo.sql")
    if os.path.exists(dados_path):
        with open(dados_path, 'r') as f:
            dados_sql = f.read()
        for statement in dados_sql.split(';'):
            stmt = statement.strip()
            if stmt:
                cursor.execute(stmt + ';')

    conn.commit()
    print("Banco de dados inicializado com sucesso.")

except mysql.connector.Error as err:
    print(f"Erro: {err}")
    conn.rollback()

finally:
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'conn' in locals() and conn:
        conn.close()
