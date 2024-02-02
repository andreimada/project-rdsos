from scapy.all import sniff, IP, TCP, UDP


def packet_callback(packet):
    """
    Callback function that processes each captured packet.
    """
    if not packet.haslayer(IP):
        return  # Only process IP packets

    ip_src = packet[IP].src
    ip_dst = packet[IP].dst
    proto = packet[IP].proto

    if packet.haslayer(TCP) or packet.haslayer(UDP):
        # Extract transport layer protocol details
        src_port = packet.sport
        dst_port = packet.dport

        # Check for HTTP (port 80) and attempt to extract payload
        if dst_port == 80:
            payload = packet.load if packet.haslayer(Raw) else None
        else:
            payload = None

        protocol = "TCP" if packet.haslayer(TCP) else "UDP"
        print(f"Packet: {ip_src}:{src_port} -> {ip_dst}:{dst_port} | {protocol}", end="")

        if payload:
            print(f" | Payload: {payload}")
        else:
            print("")  # Newline for non-HTTP packets
    else:
        # For non-TCP/UDP packets
        print(f"Packet: {ip_src} -> {ip_dst} | Non-TCP/UDP Packet")


def start_sniffing(interface):
    """
    Starts the packet sniffing process on the specified interface.
    """
    print(f"Starting packet sniffing on {interface}...")
    sniff(iface=interface, prn=packet_callback, store=False)


if __name__ == "__main__":
    interface = "wlan0"  # Change this to your interface
    start_sniffing(interface)
