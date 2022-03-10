#include <pcap.h>
#include <stdio.h>
#include <stdlib.h>

// Ethernet Header
struct ethheader {
    u_char  ether_dhost[6];    // Destination address
    u_char  ether_shost[6];    // Source address
    u_short ether_type;        // Type
};

// IP Header
struct ipheader {
  unsigned char      iph_ihl:4,     // IP header length
                     iph_ver:4;     // IP version
  unsigned char      iph_tos;       // Type of service
  unsigned short int iph_len;       // IP Packet length (data + header)
  unsigned short int iph_ident;     // Identification
  unsigned short int iph_flag:3,    // Fragmentation flags
                     iph_offset:13; // Flags offset
  unsigned char      iph_ttl;       // Time to Live
  unsigned char      iph_protocol;  // Protocol type
  unsigned short int iph_chksum;    // IP datagram checksum
  struct  in_addr    iph_sourceip;  // Source IP address
  struct  in_addr    iph_destip;    // Destination IP address
};

/* This function will be invoked by pcap for each captured packet.
We can process each packet inside the function. */
void got_packet(u_char *args, const struct pcap_pkthdr *header,
const u_char *packet) {
    printf("[📥 PACKET RECEIVED]\n");
    // Get the header information of Ethernet and IP
    struct ethheader *eth = (struct ethheader *)packet;
    struct ipheader *ip_pkt = (struct ipheader *)(packet + sizeof(struct ethheader));
    printf("    [SOURCE IP]: %s \n", inet_ntoa(ip_pkt->iph_sourceip));
    printf("    [SOURCE IP]: %s \n", inet_ntoa(ip_pkt->iph_destip));
}

int main() {
    pcap_t *handle;
    char errbuf[PCAP_ERRBUF_SIZE];
    struct bpf_program fp;
    char filter_exp[] = "icmp";
    bpf_u_int32 net;

    // Step 1: Open live pcap session on NIC with name br-129b8fcd5f6c.
    handle = pcap_open_live("br-129b8fcd5f6c", BUFSIZ, 1, 1000, errbuf);

    // Step 2: Compile filter_exp into BPF psuedo-code
    pcap_compile(handle, &fp, filter_exp, 0, net);

    if (pcap_setfilter(handle, &fp) !=0) {
        pcap_perror(handle, "[❌ ERROR]: ");
        exit(EXIT_FAILURE);
    }

    // Step 3: Capture packets
    pcap_loop(handle, -1, got_packet, NULL);
    pcap_close(handle);
    return 0;
    //Close the handle
}
// Note: don't forget to add "-lpcap" to the compilation command.
// For example: gcc -o sniff sniff.c -lpcap