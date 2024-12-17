#One Time Pad Encryption Cipher
#Christian Johnston CSEC 3312
#Fall 2024


#mickey = 01101101, 01101001, 01100011, 01101011, 01100101, 01111001
#donald = 01100100, 01101111, 01101110, 01100001, 01101100, 01100100
#sample key = 11101001, 01101110, 00110111, 01110111, 01111000, 00000000
#these values were gathered by working through the problem by hand (see additional attached document).
class OTPCipher:
    def __init__(self, message, key):
        self.message = message
        self.key = key

    def otp_encrypt(self):
        bin_message = list(self.message)
        encrypted_message = []
        bin_key = []
        for i in range(len(bin_message)):
            bin_message[i] = ''.join(f'{ord(bin_message[i]):08b}') #convert to binary strings of 8 bit length

            temp = int(bin_message[i], 2) ^ int(self.key[i], 2) #xor

            encrypted_message.append(f'{temp:0{len(bin_message)}b}')

        self.message = encrypted_message

    def speak_message(self):
        print(f'{self.message}')




m = "mickey"
k = ["11101001", "01101110", "00110111", "01110111", "01111000", "00000000"]

testCipher = OTPCipher(m, k)
testCipher.speak_message()
testCipher.otp_encrypt()
testCipher.speak_message()

m = "donald"
testCipher.message = m
testCipher.speak_message()
testCipher.otp_encrypt()
testCipher.speak_message()