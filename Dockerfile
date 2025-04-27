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
