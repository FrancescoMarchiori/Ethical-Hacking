#!/usr/bin/env python3

from scapy.all import *

ip = IP()

src = '10.9.0.5'
dst = '10.9.0.6'

ip.src = src
ip.dst = dst

icmp = ip/ICMP()

print('[🚀 SENDING PACKET]')
print('    [SOURCE]: {}'.format(src))
print('    [DESTINATION]: {}'.format(dst))

send(icmp, verbose = 0)
print('[📤 PACKET SENT]')