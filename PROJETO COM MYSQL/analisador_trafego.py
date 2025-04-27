from scapy.all import sniff, IP
import argparse
from collections import Counter
import mysql.connector
import os
import time

# Contadores globais
packets = []
protocol_counter = Counter()
src_ip_counter = Counter()
dst_ip_counter = Counter()

# Banco de dados
def salvar_no_mysql(total_pacotes, tcp, udp, top_origem, top_destino):
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", "senha123"),
            database=os.getenv("DB_NAME", "trafego")
        )
        cursor = conn.cursor()

        # Cria a tabela se não existir
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS estatisticas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                total_pacotes INT,
                pacotes_tcp INT,
                pacotes_udp INT,
                top_ips_origem TEXT,
                top_ips_destino TEXT
            )
        """)

        # Insere os dados
        sql = """
            INSERT INTO estatisticas (total_pacotes, pacotes_tcp, pacotes_udp, top_ips_origem, top_ips_destino)
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (
            total_pacotes,
            tcp,
            udp,
            str(top_origem),
            str(top_destino)
        )
        cursor.execute(sql, values)
        conn.commit()
        print("[+] Estatísticas salvas no MySQL com sucesso!")
    
    except mysql.connector.Error as err:
        print(f"[!] Erro ao salvar no MySQL: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def packet_callback(packet):
    proto = "N/A"
    src_ip = "N/A"
    dst_ip = "N/A"
    
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        
        if proto == 6:
            proto = "TCP"
        elif proto == 17:
            proto = "UDP"
        else:
            proto = str(proto)
        
        protocol_counter.update([proto])
        src_ip_counter.update([src_ip])
        dst_ip_counter.update([dst_ip])

    packets.append(packet)
    
    print(f"[+] Capturado: {src_ip} -> {dst_ip} | Protocolo: {proto} | Tamanho: {len(packet)} bytes")

def analisar_trafego():
    print("\n========== Estatísticas de Tráfego ==========")
    
    total_pacotes = len(packets)
    tcp = protocol_counter.get("TCP", 0)
    udp = protocol_counter.get("UDP", 0)
    
    print(f"Total de pacotes capturados: {total_pacotes}")
    print(f"Pacotes TCP: {tcp}")
    print(f"Pacotes UDP: {udp}")
    
    print("\nTop 5 IPs de Origem:")
    top_origem = src_ip_counter.most_common(5)
    for ip, count in top_origem:
        print(f"  {ip}: {count} pacotes")
    
    print("\nTop 5 IPs de Destino:")
    top_destino = dst_ip_counter.most_common(5)
    for ip, count in top_destino:
        print(f"  {ip}: {count} pacotes")
    
    salvar_no_mysql(total_pacotes, tcp, udp, top_origem, top_destino)
    print("\n=============================================\n")

def main():
    parser = argparse.ArgumentParser(description="Analisador de Tráfego de Rede")
    parser.add_argument("-i", "--interface", required=True, help="Interface de rede para captura")
    parser.add_argument("-c", "--count", type=int, default=0, help="Número de pacotes a capturar (0 para infinito)")
    args = parser.parse_args()

    print(f"[*] Iniciando captura na interface {args.interface}...")

    try:
        sniff(iface=args.interface, prn=packet_callback, store=False, count=args.count)
    except KeyboardInterrupt:
        print("\n[!] Captura interrompida pelo usuário.")
    finally:
        analisar_trafego()

if __name__ == "__main__":
    main()
