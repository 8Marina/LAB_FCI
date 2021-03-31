#lato client
from socket import *

serverName='localhost'
serverPort=12000

clientSocket=socket(AF_INET,SOCK_DGRAM)

message=input('Inserisci lettere')

clientSocket.settimeout(5)

clientSocket.sendto(message.encode('utf-8'),(serverName, serverPort))

try:
   risposta,serverAddress= clientSocket.recvfrom(2048)
   risposta=risposta.decode('utf-8')
   print(risposta)
except:
   print('Timeout scaduto:Server non raggiunibile')
finally:
   clientSocket.close()
#------------------------------------------------------------------------------------------  
#latoserver
from socket import *

serverPort=12000
serverSocket=socket(AF_INET,SOCK_DGRAM)

serverSocket.bind(('',serverPort))

print('Il server è pronto a ricevere')

vocali=['A','a','E','e','I','i','O','o','U','u']

while 1:
  message, clientAddress=serverSocket.recvfrom(2048)
  message= message.decode('utf-8')
  
  num=len(message)
  
  for j in vocali:
     num=num-message.count(j) 
  risposta= 'ci sono ' + str(num) + ' consonanti'
  risposta=risposta.encode('utf-8')
  serverSocket.sendto(risposta,clientAddress)
  
  
  
  
  
  
  
  
