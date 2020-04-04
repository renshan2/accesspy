import socket
from product import Product
import pickle

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((socket.gethostname(),4571))
    python_dictionary = {'a':1,'b':2}
    pickled_dictionary = pickle.dumps(python_dictionary)
    
    custom_object = Product('P024', 'Torch', 13)
    #print("custom_object:",custom_object)
    pickled_object = pickle.dumps(custom_object)                        
    
    s.listen(5)
    print('Server is up. Listening for connections...\n')
    client, address = s.accept()
    print('Connection to', address, 'estabilished\n')
    print('Client object:', client, '\n')

    #client.send(bytes(str(python_dictionary), 'utf-8'))
    #print("dictionary:",bytes(str(python_dictionary), 'utf-8'), '\n')
    #client.send(python_dictionary)
    client.send(pickled_dictionary)
    #print("custom_object:",bytes(str(custom_object),'utf-8'),'\n')
    #client.send(bytes(str(custom_object), 'utf-8'))
    
    #client.send(custom_dictionary)
    client.send(pickled_object)
