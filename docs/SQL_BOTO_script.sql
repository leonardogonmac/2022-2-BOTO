create DATABASE BOT;
use BOT;

CREATE TABLE professor(
id INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(50) NOT NULL,
plano_de_ensino VARCHAR(100) ,
email VARCHAR(50),
matricula VARCHAR(12),
senha VARCHAR(30)
);

CREATE TABLE alunos(
id INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(50) NOT NULL,
matricula VARCHAR (12) NOT NULL,
matriculaProfessor VARCHAR(12)
);

CREATE TABLE conteudos(
id INT PRIMARY KEY AUTO_INCREMENT,
titulo VARCHAR(70) NOT NULL,
link VARCHAR(100) NOT NULL,
link_extra VARCHAR(100),
matriculaProfessor VARCHAR(12)
);

CREATE TABLE conteudos_enviados(
id INT PRIMARY KEY AUTO_INCREMENT,
tituloConteudo VARCHAR(100),
matriculaAluno VARCHAR(12)
);