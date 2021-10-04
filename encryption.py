# Imports
from Crypto.Cipher import Salsa20
import time
import os

# Generating secret keys (two keys generated: one 16-byte, one 32-byte, for testing purposes)
secret_key1 = os.urandom(16)
secret_key2 = os.urandom(32)

# Encryption method, takes the data file to be encrypted as input
def encrypt_data(filename):
    # Start timer for encryption testing purposes
    encrypt_start = time.time()

    with open(filename, 'rb') as compressed_file:
        compressed_data = compressed_file.read()
    
    # Encryption algorithm used is Salsa20 
    cipher = Salsa20.new(key=secret_key1)
    encrypted_msg = cipher.nonce + cipher.encrypt(compressed_data)

    # Writes the encrypted data to a .csv file
    with open('Project Folder\Encrypted Files\encrypted_data1.csv', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_msg)
    
    # Stop the encryption timer
    encrypt_time_taken = time.time() - encrypt_start
    print("Encryption: It took " + str(round(encrypt_time_taken, 3)) + " seconds to read in, encrypt, and return the data.")

# Decryption method, takes the data file to be decrypted as input
def decrypt_data(filename):
    # Start timer for decryption testing purposes
    decrypt_start = time.time()

    with open(filename, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    
    # Deciphering the data
    msg_nonce = encrypted_data[:8]
    ciphertext = encrypted_data[8:]
    cipher = Salsa20.new(key=secret_key1, nonce=msg_nonce)
    decrypted_msg = cipher.decrypt(ciphertext)

    # Writes the decrypted data to a .csv file (this file is the output of the subsystem)
    with open('Project Folder\Decrypted Files\decrypted_data1.csv', 'wb') as decrypted_file:
        decrypted_file.write(decrypted_msg)
    
    # Stop the decryption timer
    decrypt_time_taken = time.time() - decrypt_start
    print("Decryption: It took " + str(round(decrypt_time_taken, 3)) + " seconds to read in, decrypt, and return the data.")