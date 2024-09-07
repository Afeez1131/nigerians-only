import random


class TestIP:
    IPS = {
        "local": ['127.0.0.1'],
        "NG": ['41.75.192.0', '196.220.192.0', '197.253.0.0'],
        "GB": ['98.98.142.106', '18.133.241.49', '18.133.241.49'],
        "US": ['162.254.188.0', '195.149.107.0']
    }

    ALL_IPS = [
        '127.0.0.1', '41.75.192.0', '196.220.192.0', '197.253.0.0'
    ]

    def get_ip(self, country_code):
        return random.choice(self.IPS[country_code])
