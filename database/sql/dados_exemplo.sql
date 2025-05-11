-- Inserção de dados de exemplo
INSERT INTO CONTRATACAO VALUES (1, 'CLT'), (2, 'MEI'), (3, 'CLT ou MEI');

INSERT INTO HABILIDADE VALUES
    (1, 'Poda e manejo de plantas'),
    (2, 'Irrigação e manejo do solo'),
    (3, 'Fertilidade do solo'),
    (4, 'Manutenção de jardins');

INSERT INTO CANDIDATO (nome, bairro, cidade, dt_nasc, telefone, exp_anos, cnh, hora_extra, trab_sabado, viagem_trab, id_contr)
VALUES
    ('João Silva', 'Centro', 'São Paulo', '1985-06-15', '11987654321', 5, 'B', TRUE, TRUE, TRUE, 1),
    ('Maria Oliveira', 'Vila Mariana', 'São Paulo', '1990-02-22', '11998765432', 3, 'A', FALSE, FALSE, TRUE, 2),
    ('Carlos Souza', 'Morumbi', 'São Paulo', '1987-11-10', '11999887766', 7, 'B', TRUE, FALSE, FALSE, 3);

INSERT INTO HABILIDADES_CANDIDATO (id_candidato, id_hab)
VALUES
    (1, 1), (1, 2), (2, 3), (3, 4);

INSERT INTO INFORMACOES_EXTRAS (id_cand, certificacao, exp_ferramentas, mensagem)
VALUES
    (1, 'Curso de Jardinagem', 'Experiência com trator e roçadeira', 'Gostaria de trabalhar em projetos maiores'),
    (2, 'Curso de Irrigação', 'Experiência com sistemas automatizados', 'Busco uma posição com mais desafios');
