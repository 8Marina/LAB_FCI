from socket import *
serverName='localhost'
serverPort=13000 #metto una porta diversa da quella messa nel server così mi dà errore
clientSocket=socket(AF_INET, SOCK_DGRAM)

message=input('Inserisci lettere')

clientSocket.settimeout(5)

clientSocket.sendto(message.encode('utf-8'),(serverName, serverPort))

try:
   modifiedMessage,serverAddress= clientSocket.recvfrom(2048)
   modifiedMessage=modifiedMessage.decode('utf-8')
   print(modifiedMessage)
 except:
   print('Timeout scacuto:Server non raggiungibile')
 finally: 
   clientSocket.close()
