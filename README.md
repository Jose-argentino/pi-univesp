Se o seu computador for windows, rode o comando no GitBash

### Criar um ambiente virtual
 * Abrir a pasta raiz do projeto pelo terminal;
 * Ter instalado na maquina o virtualenv (ref: https://virtualenv.pypa.io/en/latest/installation.html)
 * Rodar o comando ```virtualenv env```
 * Ativar o ambiente recém criado:
   * Se Linux: ```source env/bin/activate```;
   * Se Windows: ```source env/Scripts/activate```;
 * Em seguida, instalar as seguintes dependências:
   * ```pip install flask```;
   * ```pip install sqlalchemy```;
   * ```pip install Flask-SQLAlchemy```;
 * Por último, exportar as variáveis de ambiente:
   * ```export FLASK_APP=app```
   * ```export FLASK_ENV=development```

### Iniciar e popular o banco de dados
 * Ter instalado na maquina o MySQL Workbench, o Python3 e o pip;
 * Colocar a senha cadastrada no MySQL Workbench no arquivo **config.py** no campo _DB_PWD_;
 * Abrir o Workbench, se não estiver aberto;
 * Abrir a pasta raiz do projeto no terminal;
 * Acessar a pasta _database_ e executar o comando ```./install_db.sh``` para criar as 
tabelas do banco e dos valores das tabelas de Contratação e Habilidade que são padrão. Será inserido também dados mockados;
 


### Iniciar a aplicação 
 * Acessar a pasta raiz do projeto pelo terminal;
 * Rodar o comando ```python app.py```;
 * Acessar o endereço localhost:5000;

### Rotas Atuais
 * /
   * abre a tela de cadastro do prestador (ainda não está cadastrando no banco de dados);
 * /prestadores
   * abre a tela dos prestadores cadastrados (já está apresentando os dados mockados);
