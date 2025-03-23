create database Sistema_de_Controle_de_Dopagem;

use Sistema_de_Controle_de_Dopagem;

describe endereço;

Create table ENDEREÇO(
id_endereço int primary key auto_increment,
cep varchar(15) not null,
numero int(15)not null,
complemento varchar(15)
);

Create table Rep_Atleta(
id_Rep_Atleta int primary key auto_increment,
nome varchar(20) not null,
sobrenome varchar(60) not null
);

Create table Equipamento(
id_Equipamento int primary key auto_increment,
fabricante varchar(15)not null,
modelo varchar(20)not null
);

create table autoridade(
id_autoridade int primary key auto_increment,
AutoridadeDeTeste varchar(80) not null,
AutoridadeDeColeta varchar(80) not null,
AutoridadeDeGestao varchar(80) not null,
CoordenadorDeControleDopagem varchar(80) not null
);

create table Atleta(

id_Atleta int primary key auto_increment,
nome varchar(20) not null,
sobrenome varchar(40) not null,
nacionalidade varchar (20) not null,
telefone int not null,
Email varchar(60) not null,
Data_nascimento varchar(20) not null,
Documento varchar(20) not null,
Sexo varchar (2) not null,
id_endereço int,
FOREIGN KEY (id_endereço) REFERENCES ENDEREÇO(id_endereço)
);

alter table Atleta add column id_Rep_Atleta int;
alter table Atleta add constraint fk_Rep_Atleta
foreign key(id_Rep_Atleta) references Rep_Atleta(id_Rep_Atleta);


alter table Atleta 
add constraint fk_endereço 
foreign key (id_endereço)REFERENCES ENDEREÇO(id_endereço);


create table Teste(
id_teste int primary key auto_increment,
esporte varchar(15) not null,
disciplina varchar(15) not null,
Cordenador_Ordem_E_Teste varchar(40) not null,
Status_Competiçao boolean not null,
id_Atleta int,
id_autoridade int,
foreign key(id_Atleta) references Atleta(id_Atleta),
foreign key (id_autoridade)references autoridade(id_autoridade)
);
alter table Teste
add constraint fk_autoridade 
foreign key (id_autoridade)references autoridade(id_autoridade);

alter table Teste
add  constraint fk_Atleta
foreign key(id_Atleta) references Atleta(id_Atleta);

Create table Teste_autoridade(
id_TesteAutoridade int primary key auto_increment,
id_autoridade int,
id_teste int
);

alter table Teste_autoridade
drop constraint fk_autoridade;

describe Teste_autoridade;

alter table Teste_autoridade
add constraint fk_autoridade
foreign key (id_autoridade) references autoridade(id_autoridade);

alter table Teste_autoridade
add constraint fk_teste
foreign key(id_teste) references Teste(id_teste);

create table Amostra(
id_amostra int primary key auto_increment,
Numero_CodigoDaAmostra int not null,
InicialAtleta varchar(10) not null,
hora_selagem varchar(30) not null,
Numero_Amostra int not null,
id_equipamento int
);

alter table Amostra
add constraint fk_equipamento
foreign key (id_equipamento) references Equipamento(id_Equipamento);


create table Tipo_amostra(
id_TipoAmostra int primary key auto_increment,
DataeHora_Coleta varchar(40),
NomeDo_tipo varchar(40),
Volume int,
Densidade int,
id_amostra int
);

Alter table Tipo_amostra
add constraint fk_amostra
foreign key(id_amostra) references Amostra(id_amostra);

alter table Atleta 
modify Data_nascimento date not null;

-- Inserindo representantes de atletas
INSERT INTO Rep_Atleta (nome, sobrenome) VALUES 
('Carlos', 'Silva'),
('Mariana', 'Souza'),
('João', 'Pereira');

-- Inserindo equipamentos
INSERT INTO Equipamento (fabricante, modelo) VALUES 
('Nike', 'SensorX'),
('Adidas', 'TrackPro'),
('Puma', 'SpeedTest');

-- Inserindo autoridades
INSERT INTO autoridade (AutoridadeDeTeste, AutoridadeDeColeta, AutoridadeDeGestao, CoordenadorDeControleDopagem) VALUES 
('Autoridade Nacional de Teste', 'Coletora A', 'Gestor X', 'Coordenador Y'),
('Federação Internacional de Controle', 'Coletora B', 'Gestor Y', 'Coordenador Z');

ALTER TABLE Atleta MODIFY telefone VARCHAR(20) NOT NULL;

-- Inserindo atletas
INSERT INTO Atleta (nome, sobrenome, nacionalidade, telefone, Email, Data_nascimento, Documento, Sexo, id_endereço, id_Rep_Atleta) VALUES 
('Pedro', 'Almeida', 'Brasil', 11987654321, 'pedro@email.com', '2000-05-15', '123456789', 'M', 1, 1),
('Ana', 'Mendes', 'Portugal', 351987654321, 'ana@email.pt', '1998-08-20', '987654321', 'F', 2, 2),
('Lucas', 'Santos', 'Espanha', 349876543210, 'lucas@email.es', '1995-02-10', '112233445', 'M', 3, 3);

-- Inserindo testes
INSERT INTO Teste (esporte, disciplina, Cordenador_Ordem_E_Teste, Status_Competiçao, id_Atleta, id_autoridade) VALUES 
('Atletismo', '100m Rasos', 'Coordenador A', true, 1, 1),
('Natação', '50m Livre', 'Coordenador B', false, 2, 2);

-- Inserindo Teste_Autoridade
INSERT INTO Teste_autoridade (id_autoridade, id_teste) VALUES 
(1, 1),
(2, 2);

-- Inserindo amostras
INSERT INTO Amostra (Numero_CodigoDaAmostra, InicialAtleta, hora_selagem, Numero_Amostra, id_equipamento) VALUES 
(10001, 'PA', '12:30', 1, 1),
(10002, 'AM', '14:45', 2, 2);

-- Inserindo tipos de amostras
INSERT INTO Tipo_amostra (DataeHora_Coleta, NomeDo_tipo, Volume, Densidade, id_amostra) VALUES 
('2025-03-19 12:35', 'Sangue', 500, 1050, 1),
('2025-03-19 14:50', 'Urina', 700, 1020, 2);





