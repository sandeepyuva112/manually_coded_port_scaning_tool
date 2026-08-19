class report:
    def __init__(self, open_ports):
        self.open_ports = open_ports

    def generate_report(self):
        report = "Open Ports Report:\n"
        for port in self.open_ports:
            report += f"Port {port} is open.\n"
        return report