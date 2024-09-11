import hashlib
import random

class Transaction :
    
    def __init__(self,sign,from_client,to_client,value):
        self.nonce = None
        self.sign = sign
        self.from_client = from_client
        self.to_client = to_client
        self.value = value
        self.hash = None
        
    def set_nonce(self):
        self.nonce=random.getrandbits(100)
        
    def calc_hash(self):
        to_hash = str(self.nonce) + str(self.from_client) + str(self.value) 
        self.hash = hashlib.sha256(to_hash.encode()).hexdigest()
    
    def __str__(self):
        return (f"Transaction(\n"
                f"  sign={self.sign},\n"
                f"  from_client={self.from_client},\n"
                f"  to_client={self.to_client},\n"
                f"  value={self.value},\n"
                f"  nonce={self.nonce},\n"
                f"  hash={self.hash}\n"
                f")")
        
        
        
