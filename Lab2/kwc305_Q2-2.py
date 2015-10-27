import sys
from scapy.all import *

i = 0

while(i<15):
	a = IP()
	a.src = "10.10.111.107"
	a.dst = "10.10.111.120"
	a.flags = 0x02
	a.ttl = 10
	a.show()

	b = ICMP()
	b.type = 8
	b.id = 0x1e03
	b.seq = 0x0001

	pkt = a/b
	pkt.show()
	send(pkt)
	i+=1