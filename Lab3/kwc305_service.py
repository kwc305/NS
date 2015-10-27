import sys
from scapy.all import *

result=[]
dst_ip='10.10.111.1'


# port 53
ans,unans = sr(IP(dst=dst_ip)/UDP(dport=53),inter=0.1,retry=2,timeout=2)
result.append("port 53 is DNS")
answer = sr1(IP(dst=dst_ip)/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname='www.google.com')),verbose=8)
answer.show()

# port 67
result.append("port 67 is Bootstrap Protocol Server")
sendp(Ether(src="02:00:6f:44:0d:01")/IP(src='10.10.111.107',dst=dst_ip)/UDP(sport=68,dport=67)/DHCP(options=[("message-type","discover")]),count=3)


# port 68
ans,unans = sr(IP(dst=dst_ip)/UDP(dport=68),inter=0.1,retry=2,timeout=2)
unans.show()

print result