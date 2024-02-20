# Import necessary modules
import Sender, Signature, Des, Message_Key as message_key

# Get DES key and decrypt DES encrypted message
key = message_key.get_key()
decrypted_des = Des.des_decrypt(Sender.get_encrypted_des(), key=key)

# Get signed message, private key, decrypt signed message
signatured_message = Sender.get_signatured_message()
private_key = Signature.get_private_key()
designatured_message = Signature.rsa.decrypt(signatured_message, private_key)

# Get hash1 text
hash1_text = Sender.get_hash1_text()

# Validate message and print result
if hash1_text == designatured_message:
    print("Message is validated! " + decrypted_des)
else:
    print("!!!!!ERRORRRRRRRRRRRR!!!!")