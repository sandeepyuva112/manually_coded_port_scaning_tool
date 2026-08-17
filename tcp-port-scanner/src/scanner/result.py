class Result:
    def __init__(self, ip, port, status):
        self.ip = ip
        self.port = port
        self.status = status

    def __str__(self):
        return f"{self.ip}:{self.port} - {self.status}" 