/*Considerando que a DataBase tarefa_3 ja está criada, caso não esteja,
apenas retire os simbolos de comentario do comando a seguir*/
/*CREATE DATABASE tarefa_3*/
USE tarefa_3;

/*IMPORTAÇÃO DAS TABELAS*/
/*CRIANDO GENERICAMENTE AS TABELAS*/
drop table if exists table_1;
drop table if exists table_2;
drop table if exists table_3;
drop table if exists table_4;
drop table if exists table_5;
drop table if exists table_relatorio;
/*FIZ ASSIM POIS, CASO SEJA EXECUTADO NOVAMENTE A QUERY SE ADAPTARA AS TABELAS JA PREVIAMENTE CRIADAS*/
CREATE TABLE IF NOT EXISTS table_1 (
    `DATA` varchar(256),
    `REG_ANS` varchar(256),
    `CS_CONTA_CONTABIL` varchar(256) primary key,
    `DESCRICAO` varchar(256),
    `VL_SALDO_FINAL` varchar(256)
 );truncate table table_1;
CREATE TABLE IF NOT EXISTS table_2 (
    `DATA` varchar(256),
    `REG_ANS` varchar(256),
    `CS_CONTA_CONTABIL` varchar(256) primary key,
    `DESCRICAO` varchar(256),
    `VL_SALDO_FINAL` varchar(256)
 );truncate table table_2; 
CREATE TABLE IF NOT EXISTS table_3 (
    `DATA` varchar(256),
    `REG_ANS` varchar(256),
    `CS_CONTA_CONTABIL` varchar(256) primary key,
    `DESCRICAO` varchar(256),
    `VL_SALDO_FINAL` varchar(256)
 );truncate table table_3; 
CREATE TABLE IF NOT EXISTS table_4 (
    `DATA` varchar(256),
    `REG_ANS` varchar(256),
    `CS_CONTA_CONTABIL` varchar(256) primary key,
    `DESCRICAO` varchar(256),
    `VL_SALDO_FINAL` varchar(256)
 );truncate table table_4;
CREATE TABLE IF NOT EXISTS table_5 (
    `DATA` varchar(256),
    `REG_ANS` varchar(256),
    `CS_CONTA_CONTABIL` varchar(256) primary key,
    `DESCRICAO` varchar(256),
    `VL_SALDO_FINAL` varchar(256)
 );truncate table table_5;
CREATE TABLE IF NOT EXISTS table_relatorio (
    `Registro_ANS` varchar(256) primary key,
    `CNPJ` varchar(256),
    `RAZAO_SOCIAL` varchar(256),
    `NOME_FANTASIA` varchar(256),
    `MODALIDADE` varchar(256),
    `LOGRADOURO` varchar(256),
    `NUMERO` varchar(256),
    `COMPLEMENTO` varchar(256),
    `BAIRRO` varchar(256),
    `CIDADE` varchar(256),
    `UF` varchar(256),
    `CEP` varchar(256),
    `DDD` varchar(256),
    `TELEFONE` varchar(256),
    `FAX` varchar(256),
    `ENDERECO_ELETRONICO` varchar(256),
    `REPRESENTANTE` varchar(256),
    `CARGO_REPRESENTANTE` varchar(256),
    `DATA_REGISTRO_ANS` varchar(256)
 );truncate table table_relatorio;
 
 
/*IMPORTANDO OS ARQUIVOS CSV PARA AS TABELAS CRIADAS
PS: Deixei as tabelas em 'C:/csv/' para a importação */
LOAD DATA LOCAL INFILE 'C:/csv/1T2020.csv' INTO TABLE table_1
character set latin1
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'C:/csv/2T2020.csv' INTO TABLE table_2
character set latin1
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'C:/csv/3T2020.csv' INTO TABLE table_3
character set latin1
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'C:/csv/4T2020.csv' INTO TABLE table_4
character set latin1
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'C:/csv/1T2021.csv' INTO TABLE table_5
character set latin1
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE 'C:/csv/Relatorio_cadop.csv' INTO TABLE table_relatorio
character set latin1
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\r\n'
IGNORE 3 ROWS;

/*FIM DA QUERY DE IMPORTAÇÃO*/