#!/usr/bin/env python3

from scapy.all import *

def print_pkt(pkt):
	print('[📥 PACKET SNIFFED]')
	print('    [SOURCE]: {}'.format(pkt[IP].src))
	print('    [DESTINATION]: {}'.format(pkt[IP].dst))

print('[👃 SNIFFING...]')
pkt = sniff(iface = 'br-129b8fcd5f6c', filter = 'icmp', prn = print_pkt)