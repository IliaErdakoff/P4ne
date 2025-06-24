import ipaddress
import random

class IPv4RandomNetwork(ipaddress.IPv4Network):
    def __init__(self):
        network = random.randint(0x0B000000,0xDF000000)
        prefix = random.randint(8, 24)
        ipaddress.IPv4Network.__init__(self, ((network, prefix)), strict=False)

    def regular(self):
        return self.is_global
i=0
while i <= 10:
    g = (IPv4RandomNetwork())
    i=i+1
    print(g)

