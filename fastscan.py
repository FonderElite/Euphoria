import os,sys,platform,time
from colorama import Fore
import subprocess as sub
wi="\033[1;37m" #>>White#
rd="\033[1;31m" #>Red   #
gr="\033[1;32m" #>Green #
yl="\033[1;33m" #>Yellow#
def  slow_print(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(6. / 100)
def  slow_print2(s): 
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(7. / 100)
def banner():
 slow_print(wi + yl + '''
 ad8888888888ba
dP'         `"8b,
8  ,aaa,       "Y888a     ,aaaa,     ,aaa,  ,aa,
8  8' `8           "8baaaad""""baaaad""""baad""8b
8  8   8              """"      """"      ""    8b
8  8, ,8         ,aaaaaaaaaaaaaaaaaaaaaaaaddddd88P
8  `"""'       ,d8""
Yb,         ,ad8" 
 "Y8888888888P"
''')
 slow_print(wi + yl + '______________________')
 slow_print(wi + 'Vulnerability Scanner')
 slow_print(wi + yl + '----------------------')

banner()

def rust():
  try:
   slow_print2(wi + yl + '[!]' + wi + 'Checking some dependencies...')
   if os.path.exists('/usr/bin/rustscan'):
    slow_print(wi + gr + '[+]' + wi + 'No missing dependencies.')
    ip_save = open('ip.txt','r')
    read = ip_save.read()
    #os.system('rustscan -a ' + read + ' -- -A -sV -sC --ulimit 5000')
    os.system('rustscan -a ' + read + ' -- -vv -sV -sC -t 5')
   elif os.path.exists('/usr/bin/rustscan') == False and os.path.isfile('rustscan_2.0.1_amd64.deb'):
    slow_print2(wi + gr + '[+]' + wi + 'Unpacking rustscan_2.0.1_amd64.deb')
    os.system('sudo dpkg -i rustscan_2.0.1_amd64.deb')
    ip_saved = open('ip.txt','r')
    readf = ip_saved.read()
    if os.path.exists('/usr/bin/rustscan') == True:
     os.system('rustscan -a ' + 'localhost' + ' -- -vv -sV -sC -t 5') 
    else:
     slow_print2(wi + rd + '[+]' + wi + 'Done.')
  except:
   print(wi + rd + '[-]' + wi + 'Error.')
rust()
                