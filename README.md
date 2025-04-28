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

Execute o PowerShell dentro da pasta do projeto.

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

