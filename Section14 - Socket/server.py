import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((socket.gethostname(),4571))
s.listen(5)

print('Server is up. Listening for connections...')

clientsocket, address = s.accept()
print('Connection to', address, 'estabilished\n')
print('Client object:', clientsocket, '\n')

clientsocket.send(bytes('Hello! Welcome to socket programming.', 'utf-8'))

s.close()
