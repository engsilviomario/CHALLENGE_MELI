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

# Usa imagem oficial Python
FROM python:3.10-slim

# Define diretório de trabalho
WORKDIR /app

# Copia apenas o requirements.txt primeiro para instalar dependências
COPY requirements.txt /app/

# Atualiza pip
RUN pip install --upgrade pip

# Instala dependências
RUN pip install -r requirements.txt

# Copia o restante dos arquivos
COPY . /app

# Comando padrão (você pode sobrescrever no docker-compose)
CMD ["python", "analisador_trafego.py", "-i", "eth0", "-c", "50"]


---

## 📦 requirements.txt

scapy==2.4.5

---

## 🐳 docker-compose.yml

### Como usar:

1. Criar o arquivo docker-compose.yml no mesmo diretório do script analisador_trafego.py
2. Rodar:

docker-compose up -d

3. Entrar no Container:

docker exec -it analisador_trafego bash

3. Executar o script Python:

python analisador_trafego.py -i eth0 -c 100  #Quantaide de pacotes 100

### Para parar o container:

docker-compose down

### Customizar a interface:

docker-compose run -e INTERFACE="Ethernet" analisador

---

## ⚡ Extras (profissional):

Podemos adpatar o docker-compose e o scrippt analisador_trafego.py para capturar a interface de Rede do Host também. Pois está pegando 


