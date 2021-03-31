from socket import *
serverName='localhost'
serverPort=12000
clientSocket=socket(AF_INET, SOCK_DGRAM)

message=input('Inserisci lettere')

clientSocket.sendto(message.encode('utf-8'),(serverName, serverPort))

modifiedMessage,serverAddress= clientSocket.recvfrom(2048)
modifiedMessage=modifiedMessage.decode('utf-8')
print(modifiedMessage)
clientSocket.close()
