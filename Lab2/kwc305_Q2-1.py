import sys
from scapy.all import *


# IP
a = IP()
a.src = "10.10.111.1"
a.dst = "10.10.111.100"
a.flags = 0x02
a.ttl = 10
a.show()


# TCP
b = TCP()
b.dport = [80,53]
b.show()
pkt = a/b
pkt.show()
send(pkt)
