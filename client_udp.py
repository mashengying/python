from socket import *
serverName="localhost"
serverPort=12000
clientSocket=socket(AF_INET,SOCK_DGRAM)
message=input('input letters:')
clientSocket.sendto(message.encode(),(serverName,serverPort))
newMessage,serverAddress=clientSocket.recvfrom(2048)
print(newMessage)
print(serverAddress)