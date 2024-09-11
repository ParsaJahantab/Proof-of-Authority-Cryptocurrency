import hashlib



class Block:
    def __init__(self,previous_hash, previous_block, next_block,time_stamp,nonce,transactions,pub_key_of_validator,sign):
        self.previous_hash = previous_hash
        self.previous_block = previous_block
        self.next_block = next_block
        self.time_stamp = time_stamp
        self.nonce = nonce
        self.hash = self.calc_hash()
        self.transactions = transactions
        self.pub_key_of_validator = pub_key_of_validator
        self.sign = sign
        

    def calc_hash(self):
        to_hash = str(self.nonce) + str(self.time_stamp) + str(self.previous_hash)
        return hashlib.sha256(to_hash.encode()).hexdigest()


    def get_hash(self):
        return self.hash
    
    def get_transactions(self):
        return self.get_transactions
    
    def get_previous_block_hash(self):
        return self.previous_hash
    
    def __str__(self):
        return (f"Transaction(\n"
                f"  previous_hash ={self.previous_hash },\n"
                f"  time_stamp={self.time_stamp},\n"
                f"  nonce={self.nonce},\n"
                f"  hash={self.hash},\n"
                f"  pub_key_of_validator={self.pub_key_of_validator.to_string().hex()},\n"
                f"  sign={self.sign}\n"
                f"  number_of_transaction={len(self.transactions)}\n"
                f")")
        
        
        
        
        
        
        