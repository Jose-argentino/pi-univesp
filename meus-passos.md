cd ~/meus_projetos/meu_app

source env/bin/activate
python3 app.py
sudo apt install python-is-python3

source .venv/bin/activate
pip install -r requirements.txt
which pip
pip install flask_sqlalchemy
pip install flask_sqlalchemy --break-system-packages
python3 app.py

pip install flask
pip install sqlalchemy
pip install Flask-SQLAlchemy
export FLASK_APP=app
export FLASK_ENV=development
export FLASK_ENV=development
database/config.py  coloquei a senha em DB_PWD = "123"
chmod +x database/install_db.sh
./database/install_db.sh
    teve erro
    {
        (env) (.venv) jose@jose-RV411-RV511-E3511-S3511-RV711-E3411:~/Área de trabalho/pi-univesp-novo$ ./database/install_db.sh
        Instalando dependências no ambiente virtual...
        Requirement already satisfied: flask in ./env/lib/python3.12/site-packages (3.1.0)
        Requirement already satisfied: flask_sqlalchemy in ./env/lib/python3.12/site-packages (3.1.1)
        Requirement already satisfied: Werkzeug>=3.1 in ./env/lib/python3.12/site-packages (from flask) (3.1.3)
        Requirement already satisfied: Jinja2>=3.1.2 in ./env/lib/python3.12/site-packages (from flask) (3.1.6)
        Requirement already satisfied: itsdangerous>=2.2 in ./env/lib/python3.12/site-packages (from flask) (2.2.0)
        Requirement already satisfied: click>=8.1.3 in ./env/lib/python3.12/site-packages (from flask) (8.1.8)
        Requirement already satisfied: blinker>=1.9 in ./env/lib/python3.12/site-packages (from flask) (1.9.0)
        Requirement already satisfied: sqlalchemy>=2.0.16 in ./env/lib/python3.12/site-packages (from flask_sqlalchemy) (2.0.40)
        Requirement already satisfied: MarkupSafe>=2.0 in ./env/lib/python3.12/site-packages (from Jinja2>=3.1.2->flask) (3.0.2)
        Requirement already satisfied: greenlet>=1 in ./env/lib/python3.12/site-packages (from sqlalchemy>=2.0.16->flask_sqlalchemy) (3.2.2)
        Requirement already satisfied: typing-extensions>=4.6.0 in ./env/lib/python3.12/site-packages (from sqlalchemy>=2.0.16->flask_sqlalchemy) (4.13.2)
        Criando banco de dados...
        python3: can't open file '/home/jose/Área de trabalho/pi-univesp-novo/init.db.py': [Errno 2] No such file or directory
        (env) (.venv) jose@jose-RV411-RV511-E3511-S3511-RV711-E3411:~/Área de trabalho/pi-univesp-novo$ 
    }
    ls *.py
    ls database/*.py
python3 database/init.db.py
    teve erro
    {
        (env) (.venv) jose@jose-RV411-RV511-E3511-S3511-RV711-E3411:~/Área de trabalho/pi-univesp-novo$ python3 database/init.db.py
        Traceback (most recent call last):
        File "/home/jose/Área de trabalho/pi-univesp-novo/database/init.db.py", line 13, in <module>
            values = open('sql/init_values.sql', 'r', encoding="utf8") #Valores que precisam estar no banco para seleção
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        FileNotFoundError: [Errno 2] No such file or directory: 'sql/init_values.sql'
        (env) (.venv) jose@jose-RV411-RV511-E3511-S3511-RV711-E3411:~/Área de trabalho/pi-univesp-novo$ 
    }
    ls 
    ls database
    ls database/sql
em database/sql/init.db.py
    alterado 
    values = open('sql/init_values.sql', 'r', encoding="utf8")
    por
    values = open('database/sql/init_values.sql', 'r', encoding="utf8")
    e
    alterado 
    exemplo = open('sql/mock.sql', 'r', encoding="utf8")
    por
    exemplo = open('database/sql/mock.sql', 'r', encoding="utf8")
    e
    alterado
    schema = open('sql/schema.sql', 'r') #Criação banco de dados
    por
    schema = open('database/sql/schema.sql', 'r') #Criação banco de dados
python3 database/init.db.py
    teve erro
    (env) (.venv) jose@jose-RV411-RV511-E3511-S3511-RV711-E3411:~/Área de trabalho/pi-univesp-novo$ python3 database/init.db.py
    Traceback (most recent call last):
        File "/home/jose/Área de trabalho/pi-univesp-novo/database/init.db.py", line 17, in <module>
        cursor.execute(schema.read(), multi=True)
    TypeError: CMySQLCursor.execute() got an unexpected keyword argument 'multi'

    em database/init.db.py
    alterado 
    cursor.execute(schema.read(), multi=True)
    por
    for statement in schema.read().split(';'):
    stmt = statement.strip()
    if stmt:
        cursor.execute(stmt)
python3 database/init.db.py
    deu erro
    (env) (.venv) jose@jose-RV411-RV511-E3511-S3511-RV711-E3411:~/Área de trabalho/pi-univesp-novo$ python3 database/init.db.py
    Traceback (most recent call last):
    File "/home/jose/Área de trabalho/pi-univesp-novo/env/lib/python3.12/site-packages/mysql/connector/connection_cext.py", line 772, in cmd_query
        self._cmysql.query(
    _mysql_connector.MySQLInterfaceError: Cannot delete or update a parent row: a foreign key constraint fails

    The above exception was the direct cause of the following exception:

    Traceback (most recent call last):
    File "/home/jose/Área de trabalho/pi-univesp-novo/database/init.db.py", line 36, in <module>
        executar_sql_multiplo(schema_file)
    File "/home/jose/Área de trabalho/pi-univesp-novo/database/init.db.py", line 34, in executar_sql_multiplo
        cursor.execute(comando)
    File "/home/jose/Área de trabalho/pi-univesp-novo/env/lib/python3.12/site-packages/mysql/connector/cursor_cext.py", line 356, in execute
        self._connection.cmd_query(
    File "/home/jose/Área de trabalho/pi-univesp-novo/env/lib/python3.12/site-packages/mysql/connector/opentelemetry/context_propagation.py", line 97, in wrapper
        return method(cnx, *args, **kwargs)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/home/jose/Área de trabalho/pi-univesp-novo/env/lib/python3.12/site-packages/mysql/connector/connection_cext.py", line 781, in cmd_query
        raise get_mysql_exception(
    mysql.connector.errors.IntegrityError: 1451 (23000): Cannot delete or update a parent row: a foreign key constraint fails
    (env) (.venv) jose@jose-RV411-RV511-E3511-S3511-RV711-E3411:~/Área de trabalho/pi-univesp-novo$ 

em database/sql/cschma.sql
    acrecentrado 
    -- Exclua as tabelas que dependem de outras primeiro
    DROP TABLE IF EXISTS habilidades_candidato;
    DROP TABLE IF EXISTS informacoes_extras;
    DROP TABLE IF EXISTS candidato;
    DROP TABLE IF EXISTS outra_tabela_dependente;

    -- Agora recrie tudo normalmente:
    CREATE TABLE candidato (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100),
        ...
    );

    CREATE TABLE habilidades_candidato (
        id_cand INT,
        id_habilidade INT,
        FOREIGN KEY (id_cand) REFERENCES candidato(id) ON DELETE CASCADE
    );

    tive novo erro
            (.venv) jose@jose-RV411-RV511-E3511-S3511-RV711-E3411:~/Área de trabalho/pi-univesp-novo$ python3 database/init.db.py
        Executando:
        -- Desabilita verificação de chaves estrangeiras temporariamente
        SET FOREIGN_KEY_CHECKS=0...
        Executando:
        -- Remove tabelas na ordem correta (dos filhos para os pais)
        DROP TABLE IF EXISTS HABILIDADES_CANDID...
        Executando:
        DROP TABLE IF EXISTS INFORMACOES_EXTRAS...
        Executando:
        DROP TABLE IF EXISTS CANDIDATO...
        Executando:
        DROP TABLE IF EXISTS HABILIDADE...
        Executando:
        DROP TABLE IF EXISTS CONTRATACAO...
        Executando:
        -- Reabilita verificação de chave estrangeira
        SET FOREIGN_KEY_CHECKS=1...
        Executando:
        -- Agora recria as tabelas

        CREATE TABLE CONTRATACAO (
            id_contrato INTEGER PRIMARY KEY,
            tipo...
        Executando:
        CREATE TABLE CANDIDATO (
            id_candidato INTEGER PRIMARY KEY AUTO_INCREMENT,
            nome VARCHAR(200) ...
        Executando:
        CREATE TABLE HABILIDADE (
            id_hab INTEGER PRIMARY KEY,
            hab_nome VARCHAR(200) NOT NULL
        )...
        Executando:
        CREATE TABLE HABILIDADES_CANDIDATO (
            id_candidato INTEGER,
            id_hab INTEGER,
            PRIMARY KEY (...
        Executando:
        CREATE TABLE INFORMACOES_EXTRAS (
            id_cand INTEGER NOT NULL,
            id_info INTEGER PRIMARY KEY AUTO...
        Executando:
        INSERT INTO CONTRATACAO
            VALUES (1, 'CLT'), (2, 'MEI'), (3, 'CLT ou MEI')...
        Executando:
        INSERT INTO HABILIDADE VALUES
            (1, 'Poda e manejo de plantas'),
            (2, 'Irrigação e manejo do so...
        Executando:
        INSERT INTO candidato (nome, bairro, cidade,dt_nasc, telefone, exp_anos, cnh, hora_extra, trab_sabad...
        Traceback (most recent call last):
        File "/home/jose/Área de trabalho/pi-univesp-novo/.venv/lib/python3.12/site-packages/mysql/connector/connection_cext.py", line 772, in cmd_query
            self._cmysql.query(
        _mysql_connector.MySQLInterfaceError: Table 'bd_jardineiros.candidato' doesn't exist

        The above exception was the direct cause of the following exception:

        Traceback (most recent call last):
        File "/home/jose/Área de trabalho/pi-univesp-novo/database/init.db.py", line 42, in <module>
            executar_sql_multiplo(exemplo_file)
        File "/home/jose/Área de trabalho/pi-univesp-novo/database/init.db.py", line 13, in executar_sql_multiplo
            cursor.execute(comando)
        File "/home/jose/Área de trabalho/pi-univesp-novo/.venv/lib/python3.12/site-packages/mysql/connector/cursor_cext.py", line 356, in execute
            self._connection.cmd_query(
        File "/home/jose/Área de trabalho/pi-univesp-novo/.venv/lib/python3.12/site-packages/mysql/connector/opentelemetry/context_propagation.py", line 97, in wrapper
            return method(cnx, *args, **kwargs)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/home/jose/Área de trabalho/pi-univesp-novo/.venv/lib/python3.12/site-packages/mysql/connector/connection_cext.py", line 781, in cmd_query
            raise get_mysql_exception(
        mysql.connector.errors.ProgrammingError: 1146 (42S02): Table 'bd_jardineiros.candidato' doesn't exist
        (.venv) jose@jose-RV411-RV511-E3511-S3511-RV711-E3411:~/Área de trabalho/pi-univesp-novo$ 

tive novo erro
        (.venv) jose@jose-RV411-RV511-E3511-S3511-RV711-E3411:~/Área de trabalho/pi-univesp-novo$ python3 database/init.db.py
        Traceback (most recent call last):
        File "/home/jose/Área de trabalho/pi-univesp-novo/.venv/lib/python3.12/site-packages/mysql/connector/connection_cext.py", line 354, in _open_connection
            self._cmysql.connect(**cnx_kwargs)
        _mysql_connector.MySQLInterfaceError: Access denied for user 'seu_usuario'@'localhost'

        The above exception was the direct cause of the following exception:

        Traceback (most recent call last):
        File "/home/jose/Área de trabalho/pi-univesp-novo/database/init.db.py", line 17, in <module>
            conn = mysql.connector.connect(
                ^^^^^^^^^^^^^^^^^^^^^^^^
        File "/home/jose/Área de trabalho/pi-univesp-novo/.venv/lib/python3.12/site-packages/mysql/connector/pooling.py", line 322, in connect
            return CMySQLConnection(*args, **kwargs)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/home/jose/Área de trabalho/pi-univesp-novo/.venv/lib/python3.12/site-packages/mysql/connector/connection_cext.py", line 142, in __init__
            self.connect(**kwargs)
        File "/home/jose/Área de trabalho/pi-univesp-novo/.venv/lib/python3.12/site-packages/mysql/connector/abstracts.py", line 1605, in connect
            self._open_connection()
        File "/home/jose/Área de trabalho/pi-univesp-novo/.venv/lib/python3.12/site-packages/mysql/connector/connection_cext.py", line 360, in _open_connection
            raise get_mysql_exception(
        mysql.connector.errors.ProgrammingError: 1698 (28000): Access denied for user 'seu_usuario'@'localhost'
        (.venv) jose@jose-RV411-RV511-E3511-S3511-RV711-E3411:~/Área de trabalho/pi-univesp-novo$ 
outro erro
    (.venv) jose@jose-RV411-RV511-E3511-S3511-RV711-E3411:~/Área de trabalho/pi-univesp-novo$ python3 database/init.db.py
    Executando: -- Desabilita verificação de chaves estrangeiras temporariamente
    Executando: DROP TABLE IF EXISTS...
    Executando: -- Reabilita verificação de chave estrangeira
    Traceback (most recent call last):
    File "/home/jose/Área de trabalho/pi-univesp-novo/database/init.db.py", line 43, in <module>
        with open("database/schema.sql", 'r') as f:
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    FileNotFoundError: [Errno 2] No such file or directory: 'database/schema.sql'
    (.venv) jose@jose-RV411-RV511-E3511-S3511-RV711-E3411:~/Área de trabalho/pi-univesp-novo$ 

nano database/sql/dados_exemplo.sql

outro erro 
    (.venv) jose@jose-RV411-RV511-E3511-S3511-RV711-E3411:~/Área de trabalho/pi-univesp-novo$ python3 database/init.db.py
    Executando: -- Desabilita verificação de chaves estrangeiras temporariamente
    Executando: DROP TABLE IF EXISTS...
    Executando: -- Reabilita verificação de chave estrangeira
    Executando: -- Criação das tabelas
    Traceback (most recent call last):
    File "/home/jose/Área de trabalho/pi-univesp-novo/.venv/lib/python3.12/site-packages/mysql/connector/connection_cext.py", line 772, in cmd_query
        self._cmysql.query(
    _mysql_connector.MySQLInterfaceError: Commands out of sync; you can't run this command now

    The above exception was the direct cause of the following exception:

    Traceback (most recent call last):
    File "/home/jose/Área de trabalho/pi-univesp-novo/database/init.db.py", line 51, in <module>
        cursor.execute(dados_completos)
    File "/home/jose/Área de trabalho/pi-univesp-novo/.venv/lib/python3.12/site-packages/mysql/connector/cursor_cext.py", line 356, in execute
        self._connection.cmd_query(
    File "/home/jose/Área de trabalho/pi-univesp-novo/.venv/lib/python3.12/site-packages/mysql/connector/opentelemetry/context_propagation.py", line 97, in wrapper
        return method(cnx, *args, **kwargs)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/home/jose/Área de trabalho/pi-univesp-novo/.venv/lib/python3.12/site-packages/mysql/connector/connection_cext.py", line 781, in cmd_query
        raise get_mysql_exception(
    mysql.connector.errors.DatabaseError: 2014 (HY000): Commands out of sync; you can't run this command now
    (.venv) jose@jose-RV411-RV511-E3511-S3511-RV711-E3411:~/Área de trabalho/pi-univesp-novo$ 

novo erro
    (.venv) jose@jose-RV411-RV511-E3511-S3511-RV711-E3411:~/Área de trabalho/pi-univesp-novo$ mysql -u root -p
    Enter password: 
    Welcome to the MariaDB monitor.  Commands end with ; or \g.
    Your MariaDB connection id is 77
    Server version: 10.11.11-MariaDB-0ubuntu0.24.04.2 Ubuntu 24.04

    Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

    MariaDB [(none)]> 

CREATE DATABASE pi_univesp DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

(.venv) jose@jose-RV411-RV511-E3511-S3511-RV711-E3411:~/Área de trabalho/pi-univesp-novo$ python3 database/init.db.py
Executando: -- Desabilita verificação de chaves estrangeiras temporariamente
Executando: DROP TABLE IF EXISTS...
Executando: -- Reabilita verificação de chave estrangeira
Executando: -- Criação das tabelas
Traceback (most recent call last):
  File "/home/jose/Área de trabalho/pi-univesp-novo/database/init.db.py", line 39, in <module>
    for result in cursor.execute(schema_sql, multi=True):
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: CMySQLCursor.execute() got an unexpected keyword argument 'multi'

outo erro
    Executando: -- Desabilita verificação de chaves estrangeiras temporariamente
    Executando: DROP TABLE IF EXISTS...
    Executando: -- Reabilita verificação de chave estrangeira
    Executando: -- Criação das tabelas
    Executando: -- Desabilita verificação de chaves estrangeiras temporariam...
    Executando: -- Remove tabelas na ordem correta (dos filhos para os pais)...
    Erro: 1051: Unknown table 'pi_univesp.HABILIDADES_CANDIDATO'

outro erro 
        (.venv) jose@jose-RV411-RV511-E3511-S3511-RV711-E3411:~/Área de trabalho/pi-univesp-novo$ python3 database/init.db.py
    Executando: -- Desabilita verificação de chaves estrangeiras temporariamente
    Executando: DROP TABLE IF EXISTS...
    Executando: -- Reabilita verificação de chave estrangeira
    Executando: -- Criação das tabelas
    Executando: -- Desabilita verificação de chaves estrangeiras temporariam...
    Executando: -- Remove tabelas na ordem correta (dos filhos para os pais)...
    Erro: 1051: Unknown table 'pi_univesp.HABILIDADES_CANDIDATO'
    (.venv) jose@jose-RV411-RV511-E3511-S3511-RV711-E3411:~/Área de trabalho/pi-univesp-novo$ 
outro erro
    (.venv) jose@jose-RV411-RV511-E3511-S3511-RV711-E3411:~/Área de trabalho/pi-univesp-novo$ python3 database/init.db.py
    Erro ao criar banco: 1007: Can't create database 'pi_univesp'; database exists
outro erro
    (.venv) jose@jose-RV411-RV511-E3511-S3511-RV711-E3411:~/Área de trabalho/pi-univesp-novo$ python3 database/init.db.py
    File "/home/jose/Área de trabalho/pi-univesp-novo/database/init.db.py", line 25
    try:
    IndentationError: unexpected indent 

*******

finalmente
    (.venv) jose@jose-RV411-RV511-E3511-S3511-RV711-E3411:~/Área de trabalho/pi-univesp-novo$ python3 database/init.db.py
    Banco de dados 'pi_univesp' já existe. Continuando...
    Executando: -- Desabilita verificação de chaves estrangeiras temporariamente
    Executando: DROP TABLE IF EXISTS...
    Executando: -- Reabilita verificação de chave estrangeira
    Executando: -- Criação das tabelas
    Executando: -- Inserção de dados de exemplo (se existir)
    Banco de dados inicializado com sucesso.

*****
******
python app.py
(.venv) jose@jose-RV411-RV511-E3511-S3511-RV711-E3411:~/Área de trabalho/pi-univesp-novo$ python -u "/home/jose/Área de trabalho/pi-univesp-novo/app.py"
Traceback (most recent call last):
  File "/home/jose/Área de trabalho/pi-univesp-novo/app.py", line 13, in <module>
    db = SQLAlchemy(app)
         ^^^^^^^^^^^^^^^
  File "/home/jose/Área de trabalho/pi-univesp-novo/.venv/lib/python3.12/site-packages/flask_sqlalchemy/extension.py", line 278, in __init__
    self.init_app(app)
  File "/home/jose/Área de trabalho/pi-univesp-novo/.venv/lib/python3.12/site-packages/flask_sqlalchemy/extension.py", line 374, in init_app
    engines[key] = self._make_engine(key, options, app)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jose/Área de trabalho/pi-univesp-novo/.venv/lib/python3.12/site-packages/flask_sqlalchemy/extension.py", line 665, in _make_engine
    return sa.engine_from_config(options, prefix="")
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jose/Área de trabalho/pi-univesp-novo/.venv/lib/python3.12/site-packages/sqlalchemy/engine/create.py", line 823, in engine_from_config
    return create_engine(url, **options)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<string>", line 2, in create_engine
  File "/home/jose/Área de trabalho/pi-univesp-novo/.venv/lib/python3.12/site-packages/sqlalchemy/util/deprecations.py", line 281, in warned
    return fn(*args, **kwargs)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^
  File "/home/jose/Área de trabalho/pi-univesp-novo/.venv/lib/python3.12/site-packages/sqlalchemy/engine/create.py", line 602, in create_engine
    dbapi = dbapi_meth(**dbapi_args)
            ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jose/Área de trabalho/pi-univesp-novo/.venv/lib/python3.12/site-packages/sqlalchemy/dialects/mysql/pymysql.py", line 74, in import_dbapi
    return __import__("pymysql")
           ^^^^^^^^^^^^^^^^^^^^^

python -u "/home/jose/Área de trabalho/pi-univesp-novo/app.py"
    (.venv) jose@jose-RV411-RV511-E3511-S3511-RV711-E3411:~/Área de trabalho/pi-univesp-novo$ python -u "/home/jose/Área de trabalho/pi-univesp-novo/app.py"
    Traceback (most recent call last):
    File "/home/jose/Área de trabalho/pi-univesp-novo/app.py", line 46, in <module>
        @app.route('/servico')
        ^^^^^^^^^^^^^^^^^^^^^
    File "/home/jose/Área de trabalho/pi-univesp-novo/.venv/lib/python3.12/site-packages/flask/sansio/scaffold.py", line 362, in decorator
        self.add_url_rule(rule, endpoint, f, **options)
    File "/home/jose/Área de trabalho/pi-univesp-novo/.venv/lib/python3.12/site-packages/flask/sansio/scaffold.py", line 47, in wrapper_func
        return f(self, *args, **kwargs)
            ^^^^^^^^^^^^^^^^^^^^^^^^
    File "/home/jose/Área de trabalho/pi-univesp-novo/.venv/lib/python3.12/site-packages/flask/sansio/app.py", line 657, in add_url_rule
        raise AssertionError(
    AssertionError: View function mapping is overwriting an existing endpoint function: servico


investigando

(.venv) jose@jose-RV411-RV511-E3511-S3511-RV711-E3411:~/Área de trabalho/pi-univesp-novo$ ls
app.py  database  entities  env  meus-passos.md  README.md  static  templates
