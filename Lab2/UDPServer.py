from socket import *

serverPort=12000
serverSocket=socket(AF_INET,SOCK_DGRAM)

serverSocket.bind(('',serverPort))
print('Il server è pronto a ricevere')

while 1:
    message, clientAddress=serverSocket.recvfrom(2048)
    print('Messaggio da ', clientAddress)
    
    message=message.decode('utf-8')
    modifiedMessage=message.upper()
    modifiedMessage=modifiedMessage.encode('utf-8')
    serverSocket.sendto(modifiedMessage, clientAddress)
