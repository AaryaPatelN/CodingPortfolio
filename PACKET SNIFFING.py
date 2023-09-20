from scapy.all import sniff, Ether, IP, TCP, UDP, ICMP

def packet_callback(packet):
    if Ether in packet:
        if IP in packet:
            src_mac = packet[Ether].src
            dst_mac = packet[Ether].dst
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst

            print("Packet Details:")
            print("Source MAC:", src_mac)
            print("Destination MAC:", dst_mac)
            print("Source IP:", src_ip)
            print("Destination IP:", dst_ip)

            if TCP in packet:
                src_port = packet[TCP].sport
                dst_port = packet[TCP].dport
                print("TCP Packet:")
                print("Source Port:", src_port)
                print("Destination Port:", dst_port)

            elif UDP in packet:
                src_port = packet[UDP].sport
                dst_port = packet[UDP].dport
                print("UDP Packet:")
                print("Source Port:", src_port)
                print("Destination Port:", dst_port)

            elif ICMP in packet:
                icmp_type = packet[ICMP].type
                icmp_code = packet[ICMP].code
                print("ICMP Packet:")
                print("Type:", icmp_type)
                print("Code:", icmp_code)

            print("----------------------")

def main():
    sniff(prn=packet_callback, count=10)

if __name__ == '__main__':
    main()
