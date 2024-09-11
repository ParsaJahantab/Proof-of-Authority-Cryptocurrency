from block import Block
import socket
import threading
import pickle

block = Block("0", None, None,1212,"123",[],"pubK","sign")




def send_object(client_socket, server_address, obj):
    data = pickle.dumps(obj)
    client_socket.sendto(data, server_address)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.bind(('localhost', 65432))
server_address = ('localhost', 8081)

send_object(client_socket, server_address, block)


