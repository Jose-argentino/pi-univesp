INSERT INTO candidato (p_nome, sobrenome, bairro, cidade,dt_nasc, telefone, exp_anos, cnh, hora_extra, trab_sabado, viagem_trab, id_contr)
VALUES('Fabio', 'Viana', 'Nova Jaguariúna', 'Jaguariúna', '1989-05-27', '1996581-2356', 10, 'A', 1, 1, 0, 1),
('Renato', 'Oliveira', 'Ressaca', 'Santo Antonio de Posse', '1986-05-16', '1993468-5682', 15, 'C', 1, 1, 1, 2);

INSERT INTO habilidades_candidato
VALUES(1, 3), (1, 6), (1,10), (1,15),
(2, 5), (2,8), (2,11), (2,14);

INSERT INTO informacoes_extras (id_cand, certificacao, exp_ferramentas)
VALUES(1, 'Poda de árvores', 'Motoserra'),
(2, 'Manutenção de jardim', 'Roçadeira, enxada, soprador');