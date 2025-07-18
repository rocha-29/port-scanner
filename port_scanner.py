import socket
import threading
import argparse

open_ports = []

def print_banner():
    print("""
    =========================================
     🔍 D_R0x - Python Port Scanner
     📦 Part of Cybersecurity Portfolio
     🛡️  Use responsibly - Educational Only
    =========================================
    """)

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} is open")
            open_ports.append(port)
        sock.close()
    except:
        pass

def main():
    print_banner()

    parser = argparse.ArgumentParser(description="Simple Port Scanner by D_R0x")
    parser.add_argument("host", help="Target host to scan (IP or domain)")
    parser.add_argument("-p", "--ports", help="Port range (e.g. 1-1000)", default="1-1024")
    args = parser.parse_args()

    # Validar host
    try:
        target_ip = socket.gethostbyname(args.host)
    except socket.gaierror:
        print("[-] Host could not be resolved. Please check the domain or IP.")
        return

    # Validar rango de puertos
    try:
        start_port, end_port = map(int, args.ports.split('-'))
        if not (1 <= start_port <= 65535 and 1 <= end_port <= 65535):
            raise ValueError
        if start_port > end_port:
            print("[-] Invalid range: Start port is greater than end port.")
            return
    except:
        print("[-] Invalid port range. Use format like 1-1000")
        return

    print(f"\n[🔎] Scanning {args.host} ({target_ip}) from port {start_port} to {end_port}...\n")

    threads = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(target_ip, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Guardar resultados
    if open_ports:
        output_file = f"{args.host}_open_ports.txt"
        with open(output_file, 'w') as f:
            for port in open_ports:
                f.write(f"Port {port} is open\n")
        print(f"\n[💾] Results saved to {output_file}")
    else:
        print("\n[ℹ️] No open ports found.")

    print("\n[✅] Scan complete.")

if __name__ == "__main__":
    main()
