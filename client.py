import pickle
import socket
import ecdsa
from connection import ClientConnection
import foundation
from transaction import Transaction

def connect(client_socket,public_key):
    address , port = foundation.connect(public_key.to_string().hex())
    print(f"you are now connected to {address} and port {port}")
    connection = ClientConnection(public_key,1,None)
    data = pickle.dumps(connection)
    address =  ('localhost', port)
    client_socket.sendto(data, address)
    return port

def make_transaction(client_socket,port,private_key,public_key,to_client,value):
    transaction = Transaction(private_key.sign(b"transaction"),public_key.to_string().hex(),to_client,value)
    connection = ClientConnection(public_key,2,transaction)
    data = pickle.dumps(connection)
    address =  ('localhost', port)
    client_socket.sendto(data, address)
    
def get_balance(client_socket,port,public_key):
    connection = ClientConnection(public_key,3,None)
    data = pickle.dumps(connection)
    address =  ('localhost', port)
    client_socket.sendto(data, address)
    data, addr = client_socket.recvfrom(65507)
    balance_message = pickle.loads(data)
    print(balance_message)
    return balance_message
    
    
private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
public_key = private_key.get_verifying_key()
print(f"your public key is {public_key.to_string().hex()} and your private key is {private_key.to_string().hex()}")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 0

while True :
    client_input = input ("whats your input connect/make_transaction/balance: ")
    if client_input == "connect" :
        port = connect(client_socket,public_key)
    elif client_input == "make_transaction":
        value = float(input("value : "))
        to_client = input("to(public address) : ")
        make_transaction(client_socket,port,private_key,public_key,to_client,value)
    elif client_input == "balance":
        print(get_balance(client_socket,port,public_key))
