import os
from terminaltables import DoubleTable
from color import *

def config():
    global interfaces
    interfaces = os.popen("route | awk '/Iface/{getline; print $8}'").read()
    interfaces = interfaces.replace("\n","") 
    global gateway
    gateway = os.popen("ip route show | grep -i 'default via'| awk '{print $3 }'").read()
    gateway = gateway.replace("\n","")

def scan():
    config()
    scan = os.popen("nmap " + gateway + "/24 -n -sP").read()
    f = open('scan.txt','w')
    f.write(scan)
    f.close()
    
    devices = os.popen(" grep report scan.txt | awk '{print $5}'").read().rstrip()
    devices_mac = os.popen("grep MAC scan.txt | awk '{print $3}'").read() + os.popen("ip addr | grep 'state UP' -A1 | tail -n1 | awk '{print $2}' | cut -f1  -d'/'").read().upper().rstrip() 
    # get devices mac and localhost mac address
    devices_name = os.popen("grep MAC scan.txt | awk '{print $4 ,S$5 $6}'").read() + "\033[1;32m(This device)\033[1;m".rstrip()

    table_data = [
            ['IP Address', 'Mac Address', 'Manufacturer'],
            [devices, devices_mac, devices_name]
            ]
    table = DoubleTable(table_data)
    # Show devices found on your network
    print("[+]═══════════[ Scan Result ]═══════════[+]")
    print(light_green(table.table))
    return devices, interfaces
