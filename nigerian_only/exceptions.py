

class LocalIpException(Exception):
    """Exception raised when a local IP address is detected."""

    def __init__(self, ip, message="Local IP address detected. You need to set the WHITELISTED_IPS setting"):
        self.ip = ip
        self.message = f"{message}: {ip}"
        super().__init__(self.message)
