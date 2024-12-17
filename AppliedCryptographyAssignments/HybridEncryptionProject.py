#Hybrid Encryption Implementation
#By Christian Johnston
#Applied Cryptography CSEC 3312 Fall 2024

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

#TODO 1:  Bob generates public key / secret key with RSA
sk = rsa.generate_private_key(public_exponent=65537, key_size=2048)
pk = sk.public_key()
print(f"Bob Generates Keys")

#TODO 2:  Alice generates the session key and uses Bob's public key to encrypt the session key, then she sends the ciphertext to Bob.
def sym_key_gen():
    return os.urandom(32)

sym_key = sym_key_gen()

encrypted_sym_key = pk.encrypt(sym_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
print(f"Alice Generates Session Key")

#TODO 2b:  Alice also uses the session key to encrypt the first message: "Hello, Bob" using the AES mechanism.
m = b"Hello, Bob" #initialized data in binary literal
iv = os.urandom(16)
cipher = Cipher(algorithms.AES(sym_key), modes.CFB(iv))
encryptor = cipher.encryptor()
encrypted_m = encryptor.update(m) + encryptor.finalize()

#data transmit: encrypted_sym_key, iv, and encrypted_m
print(f"Alice encrypts message using AES with session key")
print(f"Encrypted Message: {encrypted_m}")
#TODO 3a:  Bob uses the secret key to decrypt the ciphertext and obtain the session key.

decrypted_sym_key = sk.decrypt(encrypted_sym_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

#TODO 3b: Bob uses the decrypted session key to decrypt the first message and receives "Hello, Bob".

cipher = Cipher(algorithms.AES(decrypted_sym_key), modes.CFB(iv))
decryptor = cipher.decryptor()
decrypted_m = decryptor.update(encrypted_m) + decryptor.finalize()
print(f"Bob decrypts the message")
print(f"Decrypted Message: {decrypted_m.decode()}")

#TODO 4: Bob and Alice will communicate together using the session key.
current_session_key = sym_key_gen()
round_count = 0
round_max = 5

#function for encryption
def encrypt_message(m, session_key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(session_key), modes.CFB(iv))
    encryptor = cipher.encryptor()
    encrypted_m = encryptor.update(m) + encryptor.finalize()
    return iv, encrypted_m

#function for decryption
def decrypt_message(iv, encrypted_m, session_key):
    cipher = Cipher(algorithms.AES(session_key), modes.CFB(iv))
    decryptor = cipher.decryptor()
    return decryptor.update(encrypted_m) + decryptor.finalize()

#function for RSA key exchange
def exchange_key(pk):
    new_session_key = sym_key_gen()
    encrypted_sym_key = pk.encrypt(new_session_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    return encrypted_sym_key, new_session_key

#TODO 5: After five rounds, Alice will generate the new session key and uses the same protocol to send Bob the new session key.
print("Starting communication Session.")
for round in range(1, 21): #simulating 20 rounds of messages (4 key exchanges)
    m = f"Round: {round}".encode()
    iv, encrypted_m = encrypt_message(m, current_session_key)
    print(f"Encrypted Message: {encrypted_m}")

    decrypted_m = decrypt_message(iv, encrypted_m, current_session_key)
    print(f"Decrypted Message: {decrypted_m}")

    round_count += 1

    if round_count >= round_max:
        print("Session expired, exchanging keys.")
        encrypted_sym_key, new_session_key = exchange_key(pk)

        current_session_key = sk.decrypt(encrypted_sym_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

        round_count = 0

        print("New session established.")
print("Communication ended.")