# Import necessary libraries: hashlib for creating a hash, rsa for creating public and private keys, 
# and Message\_Key for getting the message
import hashlib
import rsa
import Message_Key as message_key

def sha256_64bit_hash(message):
   # Initialize the SHA-256 hashing algorithm
   sha256_hash = hashlib.sha256()
   
   # Update the hash with the message (converted to bytes)
   sha256_hash.update(message.encode('utf-8'))
   
   # Get the full hash (a bytes object)
   full_hash = sha256_hash.digest()
   
   # Take the first 8 bytes of the full hash (64 bits)
   truncated_hash = full_hash[:8]  
   
   return truncated_hash

# Get the message
sha_text = sha256_64bit_hash(message=message_key.get_message())

# Generate RSA public and private keys (512 bits long)
(public_key, private_key) = rsa.newkeys(512)  # Key length 512 bit

def get_public_key():
   return public_key

def get_private_key():
   return private_key
