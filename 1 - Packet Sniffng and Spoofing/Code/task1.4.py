#!/usr/bin/env python3

from scapy.all import *

def spoof(pkt):
    """
    Given a received packet, spoof its address and send a reply
    """

    # Execute only if the packet is an echo request
    if pkt[ICMP].type != 8:
        return
    else:
        # Destination becomes source and viceversa
        spoof_ip = IP(src = pkt[IP].dst, dst = pkt[IP].src)

        spoof_icmp = ICMP(type = 0, id = pkt[ICMP].id, seq = pkt[ICMP].seq)

        spoof_data = pkt[Raw].load

        spoof_pkt = spoof_ip/spoof_icmp/spoof_data
        send(spoof_pkt, verbose = 0)

        print('[📤 SPOOFED PACKET SENT]')
        return

print('[👃 SNIFFING...]')
pkt = sniff(iface = 'br-129b8fcd5f6c', filter = 'icmp', prn = spoof)