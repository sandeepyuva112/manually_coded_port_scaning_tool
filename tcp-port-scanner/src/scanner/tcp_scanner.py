class Scanner:
    def __init__(self, target_ip, ports):
        self.target_ip = target_ip
        self.ports = ports

    def scan_ports(self):
        open_ports = []
        for port in self.ports:
            if self.is_port_open(port):
                open_ports.append(port)
        return open_ports

    def is_port_open(self, port):
        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout for the connection attempt
        result = sock.connect_ex((self.target_ip, port))
        sock.close()
        return result == 0