from block import Block
from transaction import Transaction
import time
class BlockChain:
    def create_genesis_block(self):
        return Block("0", None, None,1212,"123",[],"pubK","sign")

    def __init__(self):
        self.head = self.create_genesis_block()
        self.tail = self.head
        
    def create_and_add_block(self,nonce,transactions,pub_key,sign):
        block = Block(self.tail.get_hash(),self.tail,None,int(time.time()),nonce,transactions,pub_key,sign)
        self.add_block(block)
        return block

    def add_block(self, block):
        self.tail.next_block = block
        self.tail = block
    
    def calc_balance(self,public_key):
        current = self.head
        balance = 0
        while current.next_block:
            for transaction in current.transactions:
                if transaction.from_client == public_key and transaction.to_client != public_key:
                    balance = balance - transaction.value
                if transaction.to_client == public_key and transaction.from_client != public_key:
                    balance = balance + transaction.value
                print(balance)
            current = current.next_block
        return balance
    
    def check_for_hash(self,hash):
        current = self.head
        while current.next_block:
            if current.get_hash() == hash:
                return True
            current = current.next_block
            
        return False
    
    def revert(self,hash) :
        current = self.head
        while current.next_block:
            if current.get_hash == hash:
                current.next_block = None
                return True
            current = current.next_block
            
        return False
    
    def get_previous_block_hash(self):
        return self.tail.get_previous_block_hash()
    
    
    
    