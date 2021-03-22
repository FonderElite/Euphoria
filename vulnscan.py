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
def  fast_print(s): 
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / 100)
def banner():
 slow_print2(wi + '''
The Internet is a worldwide platform for sharing information. It is a community of common interests. 
No country is immune to such global challenges as cybercrime, 
hacking, and invasion of privacy.
-#Root''')
 print(wi + Fore.BLACK + rd +  '''
    .... NO! ...                  ... MNO! ...
   ..... MNO!! ...................... MNNOO! ...
 ..... MMNO! ......................... MNNOO!! .
..... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .
 ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....
    ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...
   ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....
   ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...
    ....... MMMMM..    OPPMMP    .,OMI! ....
     ...... MMMM::   o.,OPMP,.o   ::I!! ...
         .... NNM:::.,,OOPM!P,.::::!! ....
          .. MMNNNNNOOOOPMO!!IIPPO!!O! .....
         ... MMMMMNNNNOO:!!:!!IPPPPOO! ....
           .. MMMMMNNOOMMNNIIIPPPOO!! ......
          ...... MMMONNMMNNNIIIOO!..........
       ....... MN MOMMMNNNIIIIIO! OO ..........
    ......... MNO! IiiiiiiiiiiiI OOOO ...........
  ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........
   .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........
   ...... MNNNNO! .. PPPPPPPPP .. MMNON!........
      ...... OO! ................. ON! .......
 ''')
 slow_print(wi + yl + '______________________')
 slow_print(wi + 'Vulnerability Scanner')
 slow_print(wi + yl + '----------------------')

banner()
def vulnports(port):
  vp = ['http','https','ftp','ssh','telnet','netbios-ssn','dns','pop3','windows-rpc','mysql','smtp','msrpc',port]
  if os.path.isfile('scan.txt') == True:
   slow_print(wi + gr + '[+]' + wi + 'File saved as scan.txt')
   print(wi + yl + '[!]' + wi + 'Checking for Vulnerable Ports...')
   time.sleep(1.5)
   with open("scan.txt") as file: 
    data = file.read()
    for port in vp:
     if port in data:
      print(wi + gr + '[+]' + wi + 'Vulnerable port Found!' + '(' + port + ')' + '👍')
      if port == vp[1] in data:
       print(wi + yl + '[!]' + wi + 'Possible Vulnerable port: ' + '(' + port +')' + '[XSS,SQLi,XXE,CSRF etc...]')  
     else:
      print(wi + rd + '[-]' + wi + 'Vulnerable port:' + '(' + port + ')' + ' was not Found in the scan. 👎')
def main():
  try:
   slow_print2(wi + yl + '[!]' + wi + 'Checking some dependencies...')
   if os.path.exists('/usr/bin/rustscan') == True and os.path.isfile('rustscan_2.0.1_amd64.deb') == True:
    slow_print(wi + gr + '[+]' + wi + 'No missing dependencies.')
    ip_save = open('ip.txt','r')
    read = ip_save.read()
    #os.system('rustscan -a ' + read + ' -- -A -sV -sC --ulimit 5000')
    #os.system('rustscan -a ' + read + ' -- -sV -sC -A -oN scan.txt')
    #sub.call(['rustscan','-a ',read,' --',' -sV',' -sC',' -A',' scan.txt'])
    print(wi + gr + "[+]" + wi + "IP to be scanned: " + read)
    ip = '172.217.31.238'
    scan_ip = input(wi + yl + '[!]' + wi + 'Input here the IP above: ')
    string = str(read)
    scan = 'rustscan -b 1000 -a '
    output = ' -- -oN scan.txt'
    scanned =  scan  + scan_ip +  output
    os.system(scanned)
    vulnports('ms-sql-s')
   elif os.path.exists('/usr/bin/rustscan') == True and os.path.isfile('rustscan_2.0.1_amd64.deb') == False:
    slow_print(wi + rd + '[-]' + wi + 'rustscan_2.0.1_amd64.deb is missing.')
   elif os.path.exists('/usr/bin/rustscan') == False and os.path.isfile('rustscan_2.0.1_amd64.deb'):
    slow_print2(wi + gr + '[+]' + wi + 'Unpacking rustscan_2.0.1_amd64.deb')
    os.system('sudo dpkg -i rustscan_2.0.1_amd64.deb')
    ip_saved = open('ip.txt','r')
    readf = ip_saved.read()
    if os.path.exists('/usr/bin/rustscan') == True:
     file = open('ip.txt','r')
     readip = file.read()
     print(wi + gr + "[+]" + wi + "IP to be scanned: " + readip)
     ip_to_scan =  input(wi + yl + '[!]' + wi + 'Input here the IP above: ')
     scan = 'rustscan -b 1000 -a '
     output = ' -- -oN scan.txt'
     scanned =  scan  +  ip_to_scan +  output
     os.system(scanned)
     vulnports('ms-sql-s')
     readip.close()
    else:
     slow_print2(wi + rd + '[+]' + wi + 'Done.')
  except Exception:
    import pdb
    pdb.set_trace()
   print(wi + rd + '[-]' + wi + 'Error.')
if __name__ == "__main__":
    main()
#Fast Vulnerability Scanner!
