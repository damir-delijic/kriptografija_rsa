
import random

# n - number
# k - number of rounds
def miller_rabin(n, k):
    # writing n  as (2^r) * d + 1
    r = 0
    d = n - 1
    while not ( d & 1 ):
        d >>= 1
        r += 1
        
    # witness loop
    for _ in range(k):
        # pick a random integer a in the range -[2, n − 2]-
        a = random.randint(2, n - 2) # flaw: pseudorandom
        x = pow(a, d, n)
        if (x == 1 or x == n-1):
            continue
        
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if (x == 1):
                return False
            if ( x == n - 1 ):
                break
        else:
            return False
        
    return True
    #output: false if it is composite, true if it is probably prime

# generating probable primes by drawing integers at random untill one passes
# b - number of binary digits
# k - number of rounds for miller rabin
def prim_num_find(b):
    # k treba da bude funckija od b?
    if b >= 1024:
        k = 5
    else:
        k = 10

    while True:
        if miller_rabin(n := random.randrange(pow(2, b - 1) + 1, pow(2, b) - 1, 2), k):
            return n # flaws: strong probable prime, not definite. worst-case running time - infinte but with a probability of zero, complexity, accuracy? 

# assumes a > b
def gcd_euclid(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a

def find_e(fi):
    while gcd_euclid(fi, e:= random.randrange(3, fi -1, 2)) != 1:
        pass
    else:
        return e

# pretpostavlja da je poruka kraca od kljuca jer u suportnom ne bi trebalo korististi rsa za enkripciju vec rsa+ neki simetricni
def rsa_set(b):
    p = prim_num_find(b)
    q = prim_num_find(b)
    
    n = p * q
    fi = (p - 1) * (q - 1)

    e = find_e(fi)
    d = pow(e, -1, fi)
    
    return p, q, n, fi, e, d

def rsa_enc(m, n, e):
    return pow(m, e, n)

def rsa_dec(c, n, d):
    return pow(c, d, n)

def ENCRYPT_MESSAGE(plaintext, n, e):
    temp = encode_message(plaintext)
    m = int(temp)
    c = rsa_enc(m, n, e)
    return str(c)

def encode_message(string):
    encoded = ""
    for ch in string:
        temp = str(ord(ch))
        while(len(temp) % 3 != 0):
            temp = "0" + temp
        encoded = encoded +  temp
    return encoded

def DECRYPT_MESSAGE(c, n, d):
    c = int(c)
    m = rsa_dec(c, n, d)
    m = str(m)
    return decode_message(m)

def decode_message(m):
    decoded = ""
    while(len(m) % 3 != 0):
        m = "0" + m
    i = 0
    while(i < len(m)):
        temp = m[i:i+3]
        temp = int(temp)
        temp = chr(temp)
        decoded = decoded + temp
        i += 3
    return decoded

class Rsa:

    def __init__(self, b):
        self.b = b
        self.p, self.q, self.n, self.fi, self.e, self.d = rsa_set(self.b)

    def DECRYPT_MESSAGE(self, cypher):
        return DECRYPT_MESSAGE(cypher, self.n, self.d)

    def ENCRYPT_MESSAFE(self, plain):
        return ENCRYPT_MESSAGE(plain, self.n, self.e)

