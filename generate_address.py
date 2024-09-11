import os
import hashlib
import base58
from ecdsa import SigningKey, SECP256k1

# Generate a private key
private_key = SigningKey.generate(curve=SECP256k1)
private_key_bytes = private_key.to_string()

# Derive the public key
public_key = private_key.get_verifying_key()
public_key_bytes = public_key.to_string()

# Function to get the public address
def get_public_address(public_key_bytes):
    # Perform SHA-256 hashing on the public key
    sha256 = hashlib.sha256(public_key_bytes).digest()

    # Perform RIPEMD-160 hashing on the SHA-256 result
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(sha256)
    hashed_public_key = ripemd160.digest()

    # Add version byte (0x00 for mainnet)
    versioned_payload = b'\x00' + hashed_public_key

    # Perform SHA-256 hashing twice on the extended RIPEMD-160 result
    checksum = hashlib.sha256(versioned_payload).digest()
    checksum = hashlib.sha256(checksum).digest()

    # Take the first 4 bytes of the second SHA-256 hash as the checksum
    checksum = checksum[:4]

    # Add the 4 checksum bytes at the end of the extended RIPEMD-160 hash
    binary_address = versioned_payload + checksum

    # Convert the binary address to a Base58 string
    public_address = base58.b58encode(binary_address)
    
    return public_address

# Get the public address
public_address = get_public_address(public_key_bytes)

# Print keys and address
print(f"Private Key: {private_key.to_string().hex()}")
print(f"Public Key: {public_key.to_string().hex()}")
print(f"Public Address: {public_address.decode()}")
