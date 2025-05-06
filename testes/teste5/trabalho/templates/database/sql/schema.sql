-- Drop de tabelas caso existam
DROP TABLE IF EXISTS CONTRATACAO, CANDIDATO, HABILIDADE, HABILIDADES_CANDIDATO, INFORMACOES_EXTRAS CASCADE;

-- Criação da tabela CONTRATACAO
CREATE TABLE CONTRATACAO (
    id_contrato INTEGER PRIMARY KEY,
    tipo_contrato VARCHAR(45) NOT NULL
);

-- Criação da tabela CANDIDATO
CREATE TABLE CANDIDATO (
    id_candidato INTEGER PRIMARY KEY AUTO_INCREMENT,
    p_nome VARCHAR(45) NOT NULL,
    sobrenome VARCHAR(45) NOT NULL,
    bairro VARCHAR(45),
    cidade VARCHAR(45) NOT NULL,
    dt_nasc DATE,
    telefone VARCHAR(13) NOT NULL,
    exp_anos INTEGER NOT NULL,
    cnh VARCHAR(5),
    hora_extra BOOLEAN,
    trab_sabado BOOLEAN,
    viagem_trab BOOLEAN,
    id_contr INTEGER,
    FOREIGN KEY (id_contr) REFERENCES CONTRATACAO(id_contrato)
);

-- Criação da tabela HABILIDADE
CREATE TABLE HABILIDADE (
    id_hab INTEGER PRIMARY KEY,
    hab_nome VARCHAR(200) NOT NULL
);

-- Criação da tabela HABILIDADES_CANDIDATO (relacionamento entre candidato e habilidade)
CREATE TABLE HABILIDADES_CANDIDATO (
    id_candidato INTEGER,
    id_hab INTEGER,
    PRIMARY KEY (id_candidato, id_hab),
    FOREIGN KEY (id_candidato) REFERENCES CANDIDATO(id_candidato),
    FOREIGN KEY (id_hab) REFERENCES HABILIDADE(id_hab)
);

-- Criação da tabela INFORMACOES_EXTRAS
CREATE TABLE INFORMACOES_EXTRAS (
    id_cand INTEGER NOT NULL,
    id_info INTEGER PRIMARY KEY AUTO_INCREMENT,
    certificacao VARCHAR(200),
    exp_ferramentas VARCHAR(200),
    mensagem VARCHAR(200),
    FOREIGN KEY (id_cand) REFERENCES CANDIDATO(id_candidato)
);
