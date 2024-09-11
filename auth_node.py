import random
import time
import ecdsa
from node import Node
from blockchain import BlockChain
from block import Block
from transaction import Transaction
from connection import ClientConnection

import socket
import threading
import pickle
import sys



def check_transaction_validity(transaction:Transaction,node:Node):
    balance = node.blockchain.calc_balance(transaction.from_client)
    for t in node.transactions:
        if t.from_client == transaction.from_client:
            balance = balance - t.value
        if t.to_client == transaction.from_client:
            balance = balance + t.value
    if balance > transaction.value :
        return True
    return False

def listen_to_port(sock,connected_clients:set,node:Node):
    while True:
        data, addr = sock.recvfrom(65507)
        if not data:
            break
        try:
            obj = pickle.loads(data)
            print(f"Received from {addr}: {obj}")
            if isinstance(obj,Transaction):
                if not node.check_for_duplicate_transaction(obj) and check_transaction_validity(transaction=obj , node=node):
                    node.push_to_queue(obj)
                    node.propagate(sock,obj=obj)
                    print(f"transaction was propageted")
                else:
                    print(f"transaction was rejected")
                    
            elif isinstance(obj,Block):
                print(f"recived block as {obj}")
                # print(node.verify_block(block=obj))
                # print(node.check_for_duplicate_block(obj))
                if not node.check_for_duplicate_block(obj) and node.verify_block(block=obj):
                    node.blockchain.add_block(obj)
                    node.clear_queue()
                    node.propagate(sock,obj=obj)
                    print(f"block was propageted")
                else:
                    print(f"block was rejected")
            elif isinstance(obj , ClientConnection):
                print(f"recived a connection request as {obj}")
                if obj.type == 1:
                    connected_clients.add(obj.public_key.to_string().hex())
                    print(f"client was added to the list and the list is {connected_clients}")
                elif obj.type == 2:
                    connected_clients.add(obj.public_key.to_string().hex())
                    if check_transaction_validity(transaction=obj.transaction , node=node):
                        try:
                            obj.public_key.verify(obj.transaction.sign, b"transaction")
                            obj.transaction.set_nonce()
                            obj.transaction.calc_hash()
                            print(f"client made a transaction and transaction is {obj.transaction}")
                            node.push_to_queue(obj)
                            node.propagate(sock,obj=obj.transaction)
                            print(f"transaction was propagated")
                        except ecdsa.BadSignatureError:
                            pass
                    else:
                        print(f"transaction was rejected")
                        
                elif obj.type == 3:
                    print("here")
                    balance = node.blockchain.calc_balance(obj.public_key.to_string().hex())
                    print(balance)
                    balance_string = pickle.dumps(f"your balance is {balance}")
                    print(balance_string)
                    sock.sendto(balance_string, addr)
            elif isinstance(obj , str):
                print(f"recived a str  as {obj}")
                currpted_block_hash = obj.split(' ')[0]
                take_action = input("take action(y/n):")
                if take_action == "y":
                    node.blockchain.revert(currpted_block_hash)
                    node.propagate(obj)
                       
                
        except pickle.UnpicklingError:
            print(f"Failed to unpickle data from {addr}")
            


def parser():
    arguments = sys.argv[1:]
    return arguments
          
def extract_parts(filename, identifier):
    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        parts = line.split()
        if parts[0] == identifier:
            return parts[1], parts[2], parts[3]

    return None, None, None


def mine(sock,connected_clients,public_key,private_key,node:Node):
    nonce = random.getrandbits(100)
    list_of_transactions = []
    list_of_clients_to_give = []
    
    if len(connected_clients) > 5:
        list_of_clients_to_give = random.sample(list(connected_clients), 5)
    else:
        list_of_clients_to_give = list(connected_clients)
    for i in range(5):
        if len(node.transactions) == 0:
            break
        tranasction = node.transactions.pop()
        list_of_transactions.append(tranasction)
    for client in list_of_clients_to_give:
        tranasction = Transaction(private_key.sign(b"transacation"),public_key.to_string().hex(),client,value=2.0)
        tranasction.set_nonce()
        tranasction.calc_hash()
        list_of_transactions.append(tranasction)
    tranasction = Transaction(private_key.sign(b"transacation"),public_key.to_string().hex(),"burn",value=float(10-2*len(connected_clients)))
    tranasction.set_nonce()
    tranasction.calc_hash()
    list_of_transactions.append(tranasction)
    print("these transaction are gonna be in the block : ")
    for t in list_of_transactions:
        print(t)
    block = node.blockchain.create_and_add_block(nonce,list_of_transactions,public_key,private_key.sign(b"block"))
    node.propagate(sock,block)
    print(f"block was created propageted")

            
filename = 'address.txt'
identifier = parser()[0]
address, port, neighbor_port = extract_parts(filename, identifier)

private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
public_key = private_key.get_verifying_key()

node = Node (address,public_key,private_key,port,[neighbor_port])

set_of_connected_clients = set()
 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', int(port)))

print(f"is up on port {port}")

# listen_to_port(sock=sock,connected_clients=set_of_connected_clients,node=node)

listening_thread = threading.Thread(target=listen_to_port, args=(sock,set_of_connected_clients,node,))
listening_thread.start()
last_mine_time = 0
while True:
    node_input = input()
    if node_input == "mine":
        current_time = time.time()
        if (current_time - last_mine_time < 10):
            continue
        mine(sock,set_of_connected_clients,public_key,private_key,node)
        last_mine_time = time.time()