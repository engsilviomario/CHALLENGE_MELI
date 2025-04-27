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

   sudo apt update  
   sudo apt install python3 python3-pip

2. **Instalar o Scapy**

   pip3 install scapy

3. **Executar como root**

   sudo python3 analisador_trafego.py -i eth0

   (O Scapy no Linux utiliza a libpcap, que já vem instalada.)

---

## 🚀 Como Executar

python analisador_trafego.py -i "NOME_DA_INTERFACE" -c QUANTIDADE

- -i ou --interface: Nome da interface de rede (ex: "Ethernet", "Wi-Fi", eth0)
- -c ou --count: (Opcional) Número de pacotes a capturar. Use 0 para captura infinita.

### ✅ Exemplo de Uso no Windows

python analisador_trafego.py -i "Ethernet" -c 100

⚠️ Para descobrir o nome da interface:  
Abra o PowerShell ou CMD e execute:

Get-NetAdapter  
ou  
ipconfig

### ✅ Exemplo de Uso no Linux

sudo python3 analisador_trafego.py -i eth0 -c 50

---

## 📊 Resultados Apresentados

Após a captura, serão exibidas:

- Total de pacotes capturados  
- Número de pacotes por protocolo (TCP, UDP, etc.)  
- Top 5 IPs de origem  
- Top 5 IPs de destino  

---

## 🐳 Executando com Docker (Opcional)

### 🔨 Build da imagem

docker build -t analisador-trafego .

### ▶️ Executar o container

docker run --rm --net=host --privileged analisador-trafego -i eth0

⚠️ O parâmetro --privileged é necessário para permitir acesso à interface de rede.

---

## 📜 Observações Importantes

- No Windows, execute o terminal como Administrador  
- No Linux, é necessário usar sudo para capturar pacotes

---

## 🐳 Dockerfile (modelo)

FROM python:3.11-slim

RUN apt-get update && apt-get install -y tcpdump iproute2 && apt-get clean

RUN pip install scapy

COPY analisador_trafego.py /app/analisador_trafego.py

WORKDIR /app

ENTRYPOINT ["python", "analisador_trafego.py"]

---

## 📦 requirements.txt

scapy==2.4.5

---

## 🐳 docker-compose.yml

### Como usar:

1. Criar o arquivo docker-compose.yml no mesmo diretório do script analisador_trafego.py
2. Rodar:

docker-compose up

### Para parar o container:

docker-compose down

### Customizar a interface:

docker-compose run -e INTERFACE="Ethernet" analisador

---

## 🔧 Detalhes do docker-compose.yml:

volumes: Monta o diretório atual (.) dentro do container, permitindo que ele acesse o script e qualquer alteração feita no código seja refletida automaticamente.

working_dir: Define o diretório de trabalho dentro do container (onde o código será executado).

network_mode: host: Permite que o container utilize a rede do host para capturar pacotes.

privileged: true: Necessário para que o container tenha permissões suficientes para capturar pacotes de rede.
