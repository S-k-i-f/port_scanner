import socket
import ipaddress
import pyfiglet

def address_family():
    # Receives user input and checks which IP address version is being used and if it is valid.
    while True:
        address = input("\nEnter the IP address: ").strip()

        try:
            family = ipaddress.ip_address(address).version
            socket_family = socket.AF_INET if family == 4 else socket.AF_INET6
            return address, socket_family
        except ValueError:
            print("Invalid IP address. Try again.")

def scan(address, family):
    # Starts port scanning with a timeout to prevent freezing during connections.
    print(f"Scanning address: {address}...")
    for port in range(1, 1025):
        sock = socket.socket(family, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((address, port))
        
        if result == 0:
            print(f"Port {port} is open.")
            
        sock.close()
    print("Scan completed!\n")

if __name__ == "__main__":
    print(pyfiglet.figlet_format("Port Scanner"))
    address, family = address_family()
    scan(address, family)
