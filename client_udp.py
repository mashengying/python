from socket import *
serverName="81.70.242.195"
serverPort=5800
clientSocket=socket(AF_INET,SOCK_DGRAM)

while True:
    message=input('input letters:')
    clientSocket.sendto(message.encode(),(serverName,serverPort))
    newMessage,serverAddress=clientSocket.recvfrom(2048)
    print(newMessage)
    print(serverAddress)
