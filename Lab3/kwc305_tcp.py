import sys
from scapy.all import *

results = []
dst_ip = '10.10.111.1'

open_port=[]
closed_port=[]
filtered_port=[]

for port in range(1,101):

	tcp_port_scan = sr1( IP(dst=dst_ip)/TCP(dport=port,flags="S"),timeout=10)
	if tcp_port_scan.haslayer(TCP):
		if tcp_port_scan.getlayer(TCP).flags == 0x12:
			open_port.append(port)
		elif tcp_port_scan.getlayer(TCP).flags == 0x14:
			closed_port.append(port)
		elif (str(type(tcp_port_scan))== "<type 'NoneType'>"):
			filtered_port.append(port)

print "Opened: ",open_port
print "Closed: ", closed_port
print "FIltered: ",filtered_port
		