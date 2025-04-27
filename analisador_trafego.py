from scapy.all import sniff, IP
import argparse
from collections import Counter

# Contadores globais
packets = []
protocol_counter = Counter()
src_ip_counter = Counter()
dst_ip_counter = Counter()

def packet_callback(packet):
    proto = "N/A"
    src_ip = "N/A"
    dst_ip = "N/A"
    
    # Verifica se o pacote tem camada IP
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        
        # Ajusta protocolo para nome
        if proto == 6:
            proto = "TCP"
        elif proto == 17:
            proto = "UDP"
        else:
            proto = str(proto)
        
        # Conta protocolos e IPs
        protocol_counter.update([proto])
        src_ip_counter.update([src_ip])
        dst_ip_counter.update([dst_ip])

    packets.append(packet)
    
    print(f"[+] Capturado: {src_ip} -> {dst_ip} | Protocolo: {proto} | Tamanho: {len(packet)} bytes")

def analisar_trafego():
    print("\n========== Estatísticas de Tráfego ==========")
    
    # Número total de pacotes
    print(f"Total de pacotes capturados: {len(packets)}")
    
    # Número de pacotes por protocolo
    print("\nPacotes por protocolo:")
    for proto, count in protocol_counter.items():
        print(f"  {proto}: {count} pacotes")
    
    # Top 5 IPs de origem
    print("\nTop 5 IPs de Origem:")
    for ip, count in src_ip_counter.most_common(5):
        print(f"  {ip}: {count} pacotes")
    
    # Top 5 IPs de destino
    print("\nTop 5 IPs de Destino:")
    for ip, count in dst_ip_counter.most_common(5):
        print(f"  {ip}: {count} pacotes")
    
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