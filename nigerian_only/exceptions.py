

class LocalIpException(Exception):
    """Exception raised when a local IP address is detected."""

    def __init__(self, ip, message="Local IP addresses are not allowed"):
        self.ip = ip
        self.message = f"{message}: {ip}"
        super().__init__(self.message)
