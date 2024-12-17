#ElGamal Implementation Homework
#by Christian Johnston
#Applied Cryptography CSEC 3312  Fall 2024

#TASK 2 In ElGamal, given the prime p=31:
#a. Choose an appropriate e1 and d, then calculate e2.
# d is a member of group G = <Zp*, x> such that 1 <= d <= p - 2
# e1 is a primitive root in the group G = <Zp*, x>
# e2 = e1^d mod p
p = 31

#to choose an e1, we need to find primitive roots of p.
#make sure e1 is in {1, 2, ... 30}
#p = 31, p - 1 = 30 = 2 * 3 * 5
#lets choose 3 for e1.
e1 = 3

#to choose a d, we need any integer that satisfies 1 <= d <= p - 2
#lets just say 12.
d = 12

#finally we need to calculate an e2.
#e2 = e1^d mod p
e2 = pow(e1, d, p)  #e2 = 8

#b. Encrypt the message “HELLO”; use 00 to 25 for encoding. Use different blocks to make P < p.
encode_map = {i: chr(65 + i) for i in range(26)}
encode_map[26] = ' '

def encode(values):
    return ''.join(encode_map[v] for v in values)

def decode(encoded_str):
    return [ord(c) - 65 if c != ' ' else 26 for c in encoded_str]

message = 'HELLO'

m = decode(message)
print(m)

#encryption
P_size = 3
blocks = [m[i:i + P_size] for i in range(0, len(m), P_size)]

encrypted_m = []

#we need to choose a random integer, r, in G.  Lets say 5
r = 5

for block in blocks:
    for P in block:
        c1 = pow(e1, r, p)
        c2 = (P * pow(e2, r, p)) % p
        encrypted_m.append((c1, c2))
print(encrypted_m)

#c. Decrypt the ciphertext to obtain the plaintext.
decrypted_m = []

for (c1, c2) in encrypted_m:
    P = (c2 * pow(c1, -d, p)) % p
    decrypted_m.append(P)

print(decrypted_m)

m = encode(decrypted_m)

print(m)