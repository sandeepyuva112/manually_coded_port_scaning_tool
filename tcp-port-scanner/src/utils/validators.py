class validators:
    @staticmethod
    def validate_ip(ip_address):
        # Validate the IP address format
        parts = ip_address.split('.')
        if len(parts) != 4:
            return False
        for part in parts:
            if not part.isdigit() or not 0 <= int(part) <= 255:
                return False
        return True

    @staticmethod
    def validate_port(port):
        # Validate the port number range
        return isinstance(port, int) and 0 <= port <= 65535