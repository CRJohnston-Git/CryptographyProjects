#RSA Implementation Homework
#by Christian Johnston
#Applied Cryptography CSEC 3312  Fall 2024


#TASK 1.a
#given values: n= 221, e = 5

#p = 13, q = 17

#phi_n = (p-1)*(q-1) = 192

#5d = 1 (mod 192)
#d = (1 + 192k) / 5
#192 % 5 = 2
#2k + 1 = 0 (mod 5)
#2k = -1 (mod 5)
#2k = 4, k=2
#d = (1 + 192*2) / 5
#d = 77


#TASK 1.b

#Encoding for Values:
encode_map = {i: chr(65 + i) for i in range(26)}
encode_map[26] = ' '

def encode(values):
    return ''.join(encode_map[v] for v in values)

def decode(encoded_str):
    return [ord(c) - 65 if c != ' ' else 26 for c in encoded_str]

message = 'HOW ARE YOU'

print(message)

m = decode(message)

print(m)
#key generation (d should be secret)
n = 221
e = 5
d = 77
P_size = 3 #less than n

#split m into blocks
blocks = [m[i:i + P_size] for i in range(0, len(m), P_size)]

#encryption ( C = P^e mod n )
encrypted_m = []
for block in blocks:
    for P in block:
        C = pow(P, e, n)
        encrypted_m.append(C)

print(encrypted_m)

#decryption ( P = C^d mod n )
decrypted_m = []
for C in encrypted_m:
    P = pow(C, d, n)
    decrypted_m.append(P)

print(decrypted_m)

m = encode(decrypted_m)

print(m)

