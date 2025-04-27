# CHALLENGE_MELI

# 📡 Analisador de Tráfego de Rede

Este projeto é uma aplicação de linha de comando para captura e análise de pacotes de rede.  
Captura informações como IPs de origem e destino, protocolo e tamanho dos pacotes.

---

## ⚙️ Tecnologias Utilizadas

- Python 3.8+
- Scapy
- Npcap (Windows)
- Docker (opcional)

---

## 📥 Instalação

### Windows

1. **Instalar o Python 3.8+**  
   [Download aqui](https://www.python.org/downloads/windows/)

2. **Instalar as dependências Python**
   ```bash
   pip install scapy

Instalar o Npcap
Baixar e instalar: [https://nmap.org/npcap/](https://npcap.com/#download)
Importante: durante a instalação, marque a opção:
✔️ Install Npcap in WinPcap API-compatible Mode

### Linux (Ubuntu/Debian)

1.Instalar o Python 3.8+

sudo apt update
sudo apt install python3 python3-pip

2.Instalar Scapy

pip3 install scapy

3. Executar como root

sudo python3 analisador_trafego.py -i eth0

(Em Linux, o Scapy usa o libpcap já instalado.)


## 🚀 Como Executar:

python analisador_trafego.py -i "NOME_DA_INTERFACE" -c QUANTIDADE

  -i ou --interface: Nome da interface de rede (ex: "Ethernet", "Wi-Fi", "eth0").
  -c ou --count: (Opcional) Número de pacotes a capturar. 0 para captura infinita.

📈 Exemplo de Uso Windows

python analisador_trafego.py -i "Ethernet" -c 100

⚠️ Para descobrir o nome correto:
Abra o PowerShell ou CMD.
Rode: Get-NetAdapter ou ipconfig

📈 Exemplo de Uso Linux

sudo python3 analisador_trafego.py -i eth0 -c 50

___________________________________________________

🎯🚀 Após a captura, serão exibidas:

Total de pacotes capturados

Número de pacotes por protocolo (TCP, UDP, etc.)

Top 5 IPs de origem

Top 5 IPs de destino
___________________________________________________

OPCIONAL DOCKER


📦 Rodar via Docker (opcional)

Build da imagem:
docker build -t analisador-trafego .

Executar o container:
docker run --rm --net=host --privileged analisador-trafego -i eth0
⚠️ O parâmetro --privileged é necessário para permitir acesso a interfaces de rede.

📜 Observações Importantes
No Windows, é obrigatório rodar o terminal como Administrador.
No Linux, é obrigatório usar sudo para capturar pacotes.

🐳 Modelo Dockerfile

# Usar imagem base oficial do Python
FROM python:3.11-slim

# Atualizar o sistema e instalar ferramentas necessárias
RUN apt-get update && apt-get install -y tcpdump iproute2 && apt-get clean

# Instalar dependências do Python
RUN pip install scapy

# Copiar o script para dentro da imagem
COPY analisador_trafego.py /app/analisador_trafego.py

# Definir diretório de trabalho
WORKDIR /app

# Comando padrão (pode ser sobrescrito na hora do run)
ENTRYPOINT ["python", "analisador_trafego.py"]

📜 requirements.txt
Esse arquivo facilita a instalação das dependências necessárias para o seu projeto em um único comando.

scapy==2.4.5

🐳 docker-compose.yml

Agora, vamos usar o docker-compose para facilitar o processo de levantar o container com tudo que você precisa já configurado. Com isso, não será necessário rodar o comando docker build manualmente, apenas docker-compose up.

Como usar o docker-compose.yml:

Criar o docker-compose.yml no mesmo diretório do seu script analisador_trafego.py.

Rodar o container com o seguinte comando:

docker-compose up
Isso vai baixar a imagem do Python, instalar o Scapy, copiar o script para dentro do container e executar o analisador_trafego.py.

Para parar o container, use:

docker-compose down

🧠 você pode customizar mais ainda a execução
Variar a interface: Quando for rodar o docker-compose, você pode sobrescrever a interface de rede que o script vai usar, por exemplo:

docker-compose run -e INTERFACE="Ethernet" analisador
