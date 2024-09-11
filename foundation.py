
import random


set_of_ports = (8081,8082,8083,8084,8085,8086,8086,8087,8088,8089,8090)
port_to_Node={
    "1DhEZoyo64moNr8VmJifBSQpfmND4A9YNQ" : 8081,
    "18vcKDSPUBgzmQoFbwKQFKZ3q2m8bjd36q" : 8082,
    "1Dbd5QoB7R4LKe7ZKt1iZP5nE9TxsJmosQ" : 8083,
    # "12ZtFNCm8mnzWXuQoXeDeUmVukc34htf81" : 8084,
    # "1BsaK9sQr35QEfeffMCiriCHxoDg5PfpHm" : 8085,
    # "1ChK4YHSTb8DPYmfcHPv9fWXC8i6Uqz2i9" : 8086,
    # "1MDhLEEUEN1fGQjdzYammy1F4RZusw5FYw" : 8087,
    "1GSJS7q7XwGw3etP619iRznxsJDUXAUqNP" : 8088,
    "1JwC7QwEgyarsviyadwfcNnnLH1zSTTzHa" : 8089,
    # "1GncYDfj5gX23Eh5uaXGgKaGJrxi4bTisN" : 8090,
    }
auth_addresses= ["1GSJS7q7XwGw3etP619iRznxsJDUXAUqNP","1JwC7QwEgyarsviyadwfcNnnLH1zSTTzHa"]
client_to_address = {}


def connect(public_key):
    if public_key in client_to_address :
        return client_to_address[public_key], port_to_Node[client_to_address[public_key]]
    address = random.choice(auth_addresses)
    port = port_to_Node[address]
    client_to_address[public_key] = port
    return address , port

    
    
    
    
        