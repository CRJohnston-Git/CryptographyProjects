#Applied Cryptography Assignment 2 RC4 Implementation
#Christian Johnston CSEC 3312
#Fall 2024


#for this assignment, I will be using a fixed 8-length key: 12345678
class RC4:



    def __init__(self, message, key):
        self.message = message
        self.key = key #inputted key


    #Key Generation and Encryption
    def encryption(self):
        s_array = []
        k_array = []
        ecm = list(self.message) #ecm stands for EnCryptedMessage



        #initial state and key bytes
        for i in range(0, 256):
            s_array.append(i)
            k_array.append(self.key[i % len(self.key)])

        j = 0

        #permuting state bytes
        for i in range(0, 256):
            j = (j + s_array[i] + int(k_array[i])) % 256
            s_array[i], s_array[j] = s_array[j], s_array[i] #tuple unpacking swap

        i = 0
        j = 0
        l = 0

        #PRGA and Encryption
        while l < len(ecm): #There is probably a better way to do this.
            i = (i + 1) % 256
            j = (j + s_array[i]) % 256
            s_array[i], s_array[j] = s_array[j], s_array[i]
            k = s_array[(s_array[i] + s_array[j]) % 256]
            ecm[l] = ord(ecm[l]) ^ k

            l += 1

        self.message = ecm

    def decryption(self):
        s_array = []
        k_array = []
        dcm = list(self.message) #dcm stands for DeCryptedMessage


        for i in range(0, 256):
            s_array.append(i)
            k_array.append(self.key[i % len(self.key)])

        j = 0


        for i in range(0, 256):
            j = (j + s_array[i] + int(k_array[i])) % 256
            s_array[i], s_array[j] = s_array[j], s_array[i]  # tuple unpacking swap

        i = 0
        j = 0
        l = 0

        # PRGA and Decryption
        while l < len(dcm):
            i = (i + 1) % 256
            j = (j + s_array[i]) % 256
            s_array[i], s_array[j] = s_array[j], s_array[i]
            k = s_array[(s_array[i] + s_array[j]) % 256]
            dcm[l] = dcm[l] ^ k

            l += 1

        self.message = ''.join([chr(i) for i in dcm])  #I had to look up how to format this.


#Broadcast for testing and display

    def speak_message(self):
        print(f'{self.message}')


#Application/Testing

k = "12345678" #test key (ideally a password submission)
m = "this is a test message" #test message (ideally a stream of data)

testCipher = RC4(m, k)

testCipher.speak_message()
testCipher.encryption()
testCipher.speak_message()
testCipher.decryption()
testCipher.speak_message()