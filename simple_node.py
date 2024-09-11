import ecdsa
from node import Node
from blockchain import BlockChain
from block import Block
from transaction import Transaction

import socket
import threading
import pickle
import sys
def check_block(block:Block,node:Node):
    for transaction in block.transactions:
        from_client = transaction.from_client
        if not from_client ==block.pub_key_of_validator.to_string().hex():
            banalce = node.blockchain.calc_balance(from_client)
            if banalce < transaction.value :
                return False
        
    return True
def listen_to_port(sock,node:Node):
    while True:
        data, addr = sock.recvfrom(65507)
        if not data:
            break
        print(addr)
        try:
            obj = pickle.loads(data)
            if isinstance(obj,Transaction):
                print(f"recived transaction as {obj}")
                if not node.check_for_duplicate_transaction(obj):
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
                    if not check_block(block=obj , node=node):
                        node.propagate(sock=sock,obj=f"error: {obj.get_hash()}")
                else:
                    print(f"block was rejected")
                
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
filename = 'address.txt'
identifier = parser()[0]
address, port, neighbor_port = extract_parts(filename, identifier)
private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
public_key = private_key.get_verifying_key()
node = Node (address,public_key,private_key,port,[neighbor_port])
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', int(port)))
print(f"is up on port {port}")
listen_to_port(sock=sock,node=node)