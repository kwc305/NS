import sys
from scapy.all import *
target = "10.10.111.2"

ans.unans = sr (IP(dst = target,ttl = (4,20),id = RandShort())/TCP = (flags = 0x02))
for snd,rcv in ans:
	print snd.ttl,rcv.src,isinstance(rcv,payload,TCP)