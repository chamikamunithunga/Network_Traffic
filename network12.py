from scapy.all import sniff
import socket
import threading

# List of known malicious IP addresses
malicious_ips = {"192.0.2.1", "203.0.113.5"}

# Function to process captured packets
def packet_handler(packet):
    # Extract source IP
    src_ip = packet[1].src if packet.haslayer(1) else None
    if src_ip:
        print(f"Packet from {src_ip}")
        check_ip(src_ip)

# Function to check for suspicious IPs
def check_ip(ip):
    if ip in malicious_ips:
        print(f"Alert! Malicious IP detected: {ip}")

# Function to scan ports
def scan_ports(ip, port_range):
    open_ports = []
    print(f"Scanning ports on {ip}...")
    for port in port_range:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    
    if open_ports:
        print(f"Open ports on {ip}: {open_ports}")
    else:
        print(f"No open ports found on {ip}.")

# Function to start sniffing and scanning
def start_monitoring(target_ip):
    # Start packet sniffing in a separate thread
    sniff_thread = threading.Thread(target=sniff, kwargs={'prn': packet_handler, 'count': 10})
    sniff_thread.start()
    
    # Start port scanning after a short delay
    threading.Timer(5.0, scan_ports, args=(target_ip, range(1, 1024))).start()

# Main function to run the tool
if __name__ == "__main__":
    target_ip = "192.0.2.2"  # Change this to the IP you want to scan
    print("Starting network monitoring...")
    start_monitoring(target_ip)


