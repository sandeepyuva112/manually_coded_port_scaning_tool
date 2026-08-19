class terminal:
    def __init__(self, open_ports):
        self.open_ports = open_ports

    def display_open_ports(self):
        print("Open Ports:")
        for port in self.open_ports:
            print(f"Port {port} is open.")