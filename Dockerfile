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
