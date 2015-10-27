import sys
from scapy.all import *

i = 0
while (i<300):
	a = IP()
	a.src = "10.10.111.107"
	a.dst = "10.10.111.120"
	a.ttl = 10
	a.flags = 0x02
	a.show()

	b = TCP()
	b.sport = RandNum(1024,65535)
	b.dport = 139
	b.seq = 0
	b.flags = 0x02
	b.show()

	pkt = z/b
	send(pkt)
	i + = 1 