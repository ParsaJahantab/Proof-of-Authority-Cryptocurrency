from collections import deque
import pickle
from blockchain import BlockChain
from block import Block
import ecdsa

from transaction import Transaction

class Node :
    def __init__(self,public_address,public_key,private_key,port,set_of_nighboring_ports):
        self.public_address = public_address
        self.public_key = public_key
        self.private_key = private_key
        self.port = port
        self.set_of_nighboring_ports = set_of_nighboring_ports
        self.transactions =deque()
        self.blockchain = BlockChain()
        
    def verify_block(self,block:Block):
        try:
            block.pub_key_of_validator.verify(block.sign, b"block")
            return True
        except ecdsa.BadSignatureError:
            return False
        
    
    def push_to_queue(self,value):
        self.transactions.append(value)
        
        
    def check_for_duplicate_transaction(self,transaction:Transaction):
        for t in self.transactions:
            if t.hash == transaction.hash:
                return True
        return False

    def check_for_duplicate_block(self,block:Block):
        return self.blockchain.check_for_hash(block.hash)
    
    def propagate(self,sock, obj):
        data = pickle.dumps(obj)
        for port in self.set_of_nighboring_ports:
            address =  ('localhost', int(port))
            sock.sendto(data, address)
            
    def clear_queue(self):
        self.transactions.clear()
        
        
        
        