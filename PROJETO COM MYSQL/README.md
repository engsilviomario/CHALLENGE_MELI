## 🧠 O que mudou:

## docker-compposer.yml
Criado o serviço db para o MySQL 8.0

analisador agora depende de db (depends_on) para garantir que o MySQL já esteja subindo

Variáveis de ambiente no analisador (DB_HOST, DB_USER, etc.)

network_mode: host só funciona no Linux! (No Windows/macOS pode ter que adaptar depois)


## requeriments.txt:

Adicionado o driver oficial para conectar Python → MySQL.

scapy

mysql-connector-python


## Atualizar analisador_trafego.py

Toda vez que o analisador_trafego.py rodar:

Captura pacotes ✅
Conta protocolos e IPs ✅
Salva as estatísticas no MySQL (tabela estatisticas) ✅

##  📢 Como usar:
Criar o arquivo docker-compose.yml no mesmo diretório do script analisador_trafego.py e do Dockerfile

Rodar:

```bash
docker-compose up -d
```

## 📦 Criando BD e Acesso (Apenas para mostrar conhecimentos):
1. Entrar no container MySQL:

```bash
docker exec -it mysql_db bash
```

2. Dentro do bash do container, entrar no MySQL:

```bash
mysql -u root -p
```
(Senha vai ser a que você definiu no docker-compose.yml, por exemplo root ou senha123.)

3. Criar o banco de dados e tabela:

```bash
CREATE DATABASE trafego;
USE trafego;

CREATE TABLE estatisticas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    total_pacotes INT,
    tcp_pacotes INT,
    udp_pacotes INT,
    top5_origem TEXT,
    top5_destino TEXT,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 🚀 Depois disso e alguns Comandos:

O analisador_trafego.py já vai conseguir conectar no banco, salvar os dados toda vez que rodar!
```bash
show databases; #Mostas as tabelas

USE trafego; #para usar a tabela de trafego

SHOW TABLES; #Vai exibir a table estatisticas.

SELECT * FROM estatisticas; #Mostra os dados da tabela estatisticas
```

## ⚡RECEBENDO OS DADOS DA TABELA FORA DO CONTAINER E ADICIOANDO MAIS DADOS NO BD MYSQL (NO HOST):

Exibindo dados:
```bash
docker exec -it mysql_db mysql -u root -p trafego -e "SELECT * FROM trafego.estatisticas;"
```
informe a senha de acesso ao bd: senha123

registrando mais dados:
```bash
docker exec -it analisador_trafego python analisador_trafego.py -i eth0 -c 1000
```

