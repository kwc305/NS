import sys
from scapy.all import *
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

dst_ip='10.10.111.1'
result = []

for port in range (1,101):
	ans,unans=sr(IP(dst=dst_ip)/UDP(dport=port),inter=0.1,retry=2,timeout=2)
	if unans!=[]:
		result.append(port)

print result