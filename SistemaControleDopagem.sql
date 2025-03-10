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





