# CHALLENGE_MELI

## 📡 Analisador de Tráfego de Rede

Aplicação de linha de comando para **captura e análise de pacotes de rede**.  
Captura informações como IPs de origem e destino, protocolo e tamanho dos pacotes.

---

## ⚙️ Tecnologias Utilizadas

- Python 3.8+
- Scapy
- Npcap (Windows)
- Docker (opcional)

---

## 📥 Instalação

### 🪟 Windows

1. **Instalar o Python 3.8+**  
   👉 https://www.python.org/downloads/windows/

2. **Instalar as dependências Python**

   pip install scapy

3. **Instalar o Npcap**  
   👉 https://npcap.com/#download  
   Importante: durante a instalação, marque a opção:  
   ✔️ Install Npcap in WinPcap API-compatible Mode

---

### 🐧 Linux (Ubuntu/Debian)

1. **Instalar o Python 3.8+**

```
   sudo apt update  
   sudo apt install python3 python3-pip
```

2. **Instalar o Scapy**

```
   pip3 install scapy
```

3. **Executar como root**

```bash
   sudo python3 analisador_trafego.py -i eth0
```

   (O Scapy no Linux utiliza a libpcap, que já vem instalada.)

---

## 🚀 Como Executar

```bash
python analisador_trafego.py -i "NOME_DA_INTERFACE" -c QUANTIDADE
```

- -i ou --interface: Nome da interface de rede (ex: "Ethernet", "Wi-Fi", eth0)
- -c ou --count: (Opcional) Número de pacotes a capturar. Use 0 para captura infinita.

### ✅ Exemplo de Uso no Windows
```
python analisador_trafego.py -i "Ethernet" -c 100
```

⚠️ Para descobrir o nome da interface:  
Abra o PowerShell ou CMD e execute:

Get-NetAdapter  ou  ipconfig

### ✅ Exemplo de Uso no Linux
```bash
sudo python3 analisador_trafego.py -i eth0 -c 50
```

---

## 📊 Resultados Apresentados

Após a captura, serão exibidas:

- Total de pacotes capturados  
- Número de pacotes por protocolo (TCP, UDP, etc.)  
- Top 5 IPs de origem  
- Top 5 IPs de destino  

---

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

Podemos adpatar o docker-compose e o scrippt analisador_trafego.py para capturar a interface de Rede do Host também.

E Customizar a interface:
docker-compose run -e INTERFACE="Ethernet" analisador


