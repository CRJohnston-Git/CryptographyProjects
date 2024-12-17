#Elliptic Curve Cryptography Implementation Homework
#by Christian Johnston
#Applied Cryptography CSEC 3312  Fall 2024
from RSAPart1 import P_size


#TASK 3:  An elliptic curve over E67(2, 3) as the elliptic curve (y^2 = x^3 + 2x + 3)
#  Bob selects e1 = (2, 22) and d = 4.
#  Alice wants to send the plaintext P = (24, 26) to Bob. She selects r = 2.
#  Write an algorithm to add two points for Alice to produce the ciphertext to send to Bob, and, algorithm for Bob to decrypt the message.

#First we need some helper functions to perform elliptic curve calculations.

def mod_inverse(a, p):
    return pow(a, -1, p)

def point_addition(P, Q, a, p):
    if P == (None, None):
        return Q
    if Q == (None, None):
        return P

    x1, y1 = P
    x2, y2 = Q

    if P != Q:
        if x1 == x2:
            return (None, None)
        lam = (y2 - y1) * mod_inverse(x2 - x1, p) % p
    else:
        if y1 == 0:
            return (None, None)
        lam = (3 * x1**2 + a) * mod_inverse(2 * y1, p) % p

    x3 = (lam**2 - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p
    return (x3, y3)

def scalar_mult(k, P, a, p):
    R = (None, None)
    Q = P

    while k > 0:
        if k % 2 == 1:
            R = point_addition(R, Q, a, p)
        Q = point_addition(Q, Q, a, p)
        k //= 2
    return R

#Definition of parameters:
p = 67
a = 2
b = 3
e1 = (2, 22)
d = 4
P = (24, 26)
r = 2

#Keygen
e2 = scalar_mult(d, e1, a, p)

#Encryption
c1 = scalar_mult(r, e1, a, p)
r_e2 = scalar_mult(r, e2, a, p)
c2 = point_addition(P, r_e2, a, p)

#Decryption
d_c1 = scalar_mult(d, c1, a, p)
neg_d_c1 = (d_c1[0], -d_c1[1] % p)
decrypted_p = point_addition(c2, neg_d_c1, a ,p)