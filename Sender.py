# Importing necessary modules
import Des
import Signature
import Message_Key as message_key

# Get plaintext message and key from Message_Key module
plaintext = message_key.get_message()
key = message_key.get_key()

# Get the RSA public key from Signature module
signature_public_key = Signature.public_key

# Encrypt the plaintext message using DES algorithm
encrypted_des = Des.des_encrypt(plaintext=plaintext, key=key)

# Compute SHA-256 hash of the plaintext message
hash1_text = Signature.sha256_64bit_hash(plaintext)

# Generate the RSA encrypted signature of the SHA-256 hash
signatured_message = Signature.rsa.encrypt(hash1_text, signature_public_key)

def get_signatured_message():
   return signatured_message

def get_hash1_text():
   return hash1_text

def get_encrypted_des():
   return encrypted_des

print("Encrypted Des :" + encrypted_des)