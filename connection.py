class ClientConnection:
    def __init__(self,public_key,type,transaction):
        self.public_key = public_key
        self.type = type
        self.transaction = transaction
        
    def __str__(self):
        return (f"ClientConnection(\n"
                f"  public_key={self.public_key.to_string().hex()},\n"
                f"  type={self.type},\n"
                f")")
        
        
        
        