import sys
from scapy.all import *


# port 68
ans,unans = sr(IP(dst=dst_ip)/UDP(dport=68),inter=0.1,retry=2,timeout=2)
unans.show()

print result