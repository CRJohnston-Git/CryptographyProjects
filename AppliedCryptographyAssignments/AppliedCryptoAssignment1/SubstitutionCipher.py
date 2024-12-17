#Substitution Cipher using Multiplicative Key
#Christian Johnston CSEC 3312
# Fall 2024
import os

class MultiSubCipher:
    def __init__(self, message, key):
        self.message = message
        self.key = key

    def encrypt_message(self):
        #remove whitespace (split and join might be better solution)
        mutable_message = list(self.message.replace(" ", ""))

        for i in range (len(mutable_message)):
            if 'a' <= mutable_message[i] <= 'z': #the if/elif statements checks for case on the characters
                mutable_message[i] = chr(((ord(mutable_message[i]) - ord('a')) * self.key) % 26 + ord('a'))

            elif 'A' <= mutable_message[i] <= 'Z':
                mutable_message[i] = chr(((ord(mutable_message[i]) - ord('A')) * self.key) % 26 + ord('A'))

            else: continue


        self.message = str(mutable_message)

#this was an interesting challenge to research.  Because multiplicative operations cannot be reversed accurately from division
#due to computers being unable to accurately deal with floating point numbers, I had to research ways to reverse a multiplicative cipher
#and found that by implementing an inverse modulo function I can reverse the encryption while preserving the integer values.
    def decrypt_message(self):
        mutable_decrypt = list(self.message.replace(",", "").replace("[", "").replace("'", "").replace("]", "")) #really quick and ugly stripping of the extra symbols, sorry
        modulo_inverse = pow(self.key, -1, 26)
        for i in range (len(mutable_decrypt)):
            if 'a' <= mutable_decrypt[i] <= 'z':
                mutable_decrypt[i] = chr(((ord(mutable_decrypt[i]) - ord('a')) * modulo_inverse) % 26 + ord('a'))
            elif 'A' <= mutable_decrypt[i] <= 'Z':
                mutable_decrypt[i] = chr(((ord(mutable_decrypt[i]) - ord('A')) * modulo_inverse) % 26 + ord('A'))
            else: continue
        self.message = str(mutable_decrypt).split()
        self.message = ''.join(self.message)  #TODO: find a way to clean up decrypted message of symbols and whitespace and convert back to proper string



    def speak_message(self):

        print(f'{self.message}')

m = "this is an exercise"
k = 15

testCipher = MultiSubCipher(m, k)
print("Original Message:")
testCipher.speak_message()
os.system('pause')

print("Encrypted Message:")
testCipher.encrypt_message()
testCipher.speak_message()
os.system("pause")

print("Decrypted Message:")
testCipher.decrypt_message()
testCipher.speak_message()
os.system("pause")
