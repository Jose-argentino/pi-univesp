Se o seu computador for windows, rode o comando no GitBash

Banco de dados
Para criar na sua máquina, precisa instalar o MySQL Workbench, o Python3 e o pip
No arquivo config.py insira as informações do seu Workbench
Entre na pasta pi-univesp/database e executar o comando './install_db.sh' para criação das 
tabelas do banco e dos valores das tabelas de Contratação e Habilidade que são padrão
 

trabalho/
├── app.py
├── database.db  ← (vai ser criado automaticamente)
└── templates/
    ├── trabalhe.html
    └── admin.html

para rodar no linux
sudo su
entre na pasta trabalho (cd trabalho), 
source .venv/bin/activate
pip install flask flask_sqlalchemy
python app.py
