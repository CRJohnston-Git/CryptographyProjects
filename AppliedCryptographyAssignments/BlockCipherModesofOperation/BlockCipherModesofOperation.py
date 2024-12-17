#AES implemented using CBC
#by Christian Johnston
#Applied Cryptography CSEC 3312
#Fall 2024

#I will be implementing the AES algorithm through the cryptography package.
#I used chatgpt to figure out the package path for implementation and mode of operation.
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

#this is used by the program to automatically select a cryptographic backend.
from cryptography.hazmat.backends import default_backend

#for unpadding the encrypted message.
from cryptography.hazmat.primitives import padding

#I am importing os to implement the random IV.
import os

#for byte encoding
import base64
import io



def AES_Encryption (text, key):
    #padding for CBC
    pad = padding.PKCS7(128).padder()
    text = pad.update(text) + pad.finalize()


    #the cryptographic backend is used to implement the algorithm
    cbcCipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    cbcEncryptor = cbcCipher.encryptor()

    return cbcEncryptor.update(text) + cbcEncryptor.finalize()

def AES_Decryption(enc_message, key):

    #same process as before, just reversed through decryptor
    cbcCipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    cbcDecryptor = cbcCipher.decryptor()

    #need to unpad the decrpytion
    padded_msg = cbcDecryptor.update(enc_message) + cbcDecryptor.finalize()
    unpad = padding.PKCS7(128).unpadder()

    return unpad.update(padded_msg) + unpad.finalize()


def AES_Encryption_File(file, key):
    #input and encoding
    with open(file, 'r') as file:
        inputString = file.read()

    inputBytes = inputString.encode('utf-8')
    buffer = io.BytesIO(inputBytes)
    encodedString = base64.b64encode(buffer.getvalue())


    #padding
    pad = padding.PKCS7(128).padder()
    encodedString = pad.update(encodedString) + pad.finalize()

    #encryption
    cbcCipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    cbcEncryptor = cbcCipher.encryptor()

    return cbcEncryptor.update(encodedString) + cbcEncryptor.finalize()

def AES_Decryption_File(enc_file, key):

    #reverse of the encryption process using decryptor
    cbcCipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    cbcDecryptor = cbcCipher.decryptor()

    padded_file = cbcDecryptor.update(enc_file) + cbcDecryptor.finalize()

    #unpad
    unpad = padding.PKCS7(128).unpadder()
    return unpad.update(padded_file) + unpad.finalize()



if __name__ == "__main__":
    #random 16 byte IV to xor with key
    iv = os.urandom(16)


    key = b'1234sfsfdsafasdf'
    plaintext = b'Hello World'
    plaintext = base64.b64encode(plaintext)
    print(plaintext)

    enc_message = AES_Encryption(plaintext, key)
    print(enc_message)
    original_message = AES_Decryption(enc_message, key)
    print(plaintext == original_message)
    print(base64.b64decode(original_message))

    enc_file = AES_Encryption_File('hello.txt', key)
    print(enc_file)

    dec_file = AES_Decryption_File(enc_file, key)
    dec_file = base64.b64decode(dec_file)
    print(dec_file)
    #here is where you would take the decoded input and write it to a file if needed.