#!/usr/bin/env python3

from scapy.all import *

dst = 'google.com'

# Starting from 1
ttl = 1

while 1:
    pkt = sr1(IP(dst = dst, ttl = ttl)/ICMP(), verbose = 0) # Verbose handle the output
    # If the TTL is exceeded
    if pkt[ICMP].type == 11 and pkt[ICMP].code == 0:
        print('[TTL = {}] IP = {}'.format(ttl, pkt.src))
        ttl += 1
    # Otherwise we reached our destination
    elif pkt[ICMP].type == 0:
        print('[REACHED W/ TTL = {}] IP = {}'.format(ttl, pkt.src))
        break