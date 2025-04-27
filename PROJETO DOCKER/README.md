## 🐳 Executando com Docker (Opcional)

## 📜 Observações Importantes

- No Windows, execute o terminal como Administrador  
- No Linux, é necessário usar sudo para capturar pacotes

## 🐳 Dockerfile (modelo)

O Dockerfile é um arquivo de texto que contém todas as instruções para construir uma imagem Docker. Pense nele como uma receita que diz ao Docker como montar seu container.

Características principais:
Define a imagem base (ex: python:3.10-slim)

Especifica dependências a serem instaladas

Configura o ambiente de execução

Determina quais arquivos serão incluídos no container

Define o comando padrão a ser executado

---

## 🐳 docker-compose.yml

O docker-compose.yml é um arquivo YAML que permite definir e gerenciar múltiplos containers como um único serviço.

Características principais:
Gerencia múltiplos containers simultaneamente

Define redes e volumes compartilhados

Configura variáveis de ambiente

Especifica portas expostas

Controla a escala dos serviços

### Como usar:

1. Criar o arquivo docker-compose.yml no mesmo diretório do script analisador_trafego.py e do Dockerfile
2. Rodar:
```bash
docker-compose up -d
```

3. Entrar no Container:
```bash
docker exec -it analisador_trafego bash
```

3. Executar o script Python:
```bash
python analisador_trafego.py -i eth0 -c 100  #Quantaide de pacotes 100
```

### Para parar o container:
```bash
docker-compose down
```

---

## 📦 requirements.txt

O arquivo requirements.txt é um arquivo essencial para projetos Python que utilizam Docker. Ele especifica todas as dependências que seu projeto precisa para funcionar corretamente.

---

## ⚡ Extras (profissional):

Podemos adpatar o docker-compose e o scrippt analisador_trafego.py para capturar a interface de Rede do Host também e uma variavél para informar a interface.

E Customizar a interface:
docker-compose run -e INTERFACE="Ethernet" analisador
