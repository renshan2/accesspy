import socket

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((socket.gethostname(),4571))

    s.listen(5)

    print('Server is up. Listening for connections...')

    client, address = s.accept()
    print('Connection to', address, 'estabilished\n')
    print('Client object:', client, '\n')
    #send message to client
    client.send(bytes('Hello Yang! Welcome to socket programming.', 'utf-8'))
