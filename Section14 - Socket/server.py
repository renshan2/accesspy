import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),4571))

s.listen(5)

print('Server is up. Listening for connections...')

client, address = s.accept()
print('Connection to', address, 'estabilished\n')
print('Client object:', client, '\n')
#sent message to client
client.send(bytes('Hello! Welcome to socket programming.', 'utf-8'))
s.close()