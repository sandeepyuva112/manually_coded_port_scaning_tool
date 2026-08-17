import socket
class Connection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = None
    def connect(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.settimeout(1)  # Set a timeout for the connection attempt
            self.sock.connect((self.host, self.port))
            return True
        except (socket.timeout, ConnectionRefusedError):
            return False
        finally:
            if self.sock:
                self.sock.close()