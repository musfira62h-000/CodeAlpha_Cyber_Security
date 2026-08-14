"""
CodeAlpha — Task 1: Basic Network Sniffer
Captures network packets and prints source/destination IPs, protocol, and payload.

Lab roles:
  - Windows host (user: hp) — traffic source / observed host IP: 192.168.1.12
  - Ubuntu host  (user: musfira00@musfira00-virtual-machine) — runs this Scapy sniffer

Requires: pip install scapy
Run on Ubuntu as: sudo python3 task1_network_sniffer.py
"""

from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw


def get_protocol_name(pkt):
    if TCP in pkt:
        return "TCP"
    if UDP in pkt:
        return "UDP"
    if ICMP in pkt:
        return "ICMP"
    if IP in pkt:
        return str(pkt[IP].proto)
    return "OTHER"


def process_packet(pkt):
    if IP not in pkt:
        return

    src = pkt[IP].src
    dst = pkt[IP].dst
    proto = get_protocol_name(pkt)

    if TCP in pkt:
        ports = f"{pkt[TCP].sport} -> {pkt[TCP].dport}"
    elif UDP in pkt:
        ports = f"{pkt[UDP].sport} -> {pkt[UDP].dport}"
    else:
        ports = "-"

    if Raw in pkt:
        payload = bytes(pkt[Raw].load)[:40]
    else:
        payload = b""

    print(f"SRC: {src:15} | DST: {dst:15} | PROTO: {proto:4} | PORTS: {ports:15} | PAYLOAD: {payload}")


def main():
    print("=" * 70)
    print("CodeAlpha Task 1 — Basic Network Sniffer (Scapy)")
    print("Capturing packets... (Press Ctrl+C to stop)")
    print("=" * 70)

    # count=30 stops after 30 packets; remove count= for continuous capture
    # iface="Wi-Fi"  # optional: set your interface name on Windows
    sniff(prn=process_packet, store=False, count=30)


if __name__ == "__main__":
    main()
