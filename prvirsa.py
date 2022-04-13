# in python, it is not necessary to represent big integers with strings?

# built-in module
import random

# n - number
# k - number of rounds

# plus prvi miler rabin koristio rucno pisanu funkciju za trazenje modula pri stepenovanju
def miller_rabin(n, k):
    # writing n  as (2^r) * d + 1
    temp = n - 1
    r = 0
    d = 0
    while( temp % 2 == 0):
        temp = temp / 2
        r += 1
    d = int(temp)
    # witness loop
    continue_witness_loop = False
    for i in range(k):
        # pick a random integer a in the range -[2, n − 2]-, pseudorandom?
        a = random.randint(2, n - 2) # flaw: pseudorandom
        x = pow(a, d, n)
        if (x == 1 or x == n-1):
            continue
        for j in range(r - 1):
            x = pow(x, 2, n)
            if ( x == n - 1 ):
                continue_witness_loop = True
                break
        if(continue_witness_loop):
            continue_witness_loop = False
            continue
        return False
    return True
    #output: false if it is composite, true if it is probably prime

# generating probable primes by drawing integers at random untill one passes
# b - number of binary digits
# k - number of rounds for miller rabin
def prim_num_find(b):
    # k treba da bude funckija od b?
    k = 10
    while True:
        n = random.randint(pow(2, b - 1), pow(2, b) - 1)
        # making sure it is odd
        if(n % 2 == 0):
            n += 1
        if miller_rabin(n, k):
            return n # flaws: strong probable prime, not definite. worst-case running time - infinte but with a probability of zero, complexity, accuracy? 

# assumes a > b
def gcd_euclid(a, b):
    if(b > a):
        return gcd_euclid(b, a)

    if b == 0:
        return a
    
    if a == 0:
        return b

    if(a % b == 0):
        return b
    return gcd_euclid(b, a % b)

def find_e(fi):
    e = random.randint(2, fi - 1)
    while gcd_euclid(fi, e) != 1:
        e = random.randint(2, fi - 1)
    return e

# pretpostavlja da je poruka kraca od kljuca jer u suportnom ne bi trebalo korististi rsa za enkripciju vec rsa+ neki simetricni
def rsa_set(b):
    p = prim_num_find(b)
    q = prim_num_find(b)
    n = p * q
    fi = (p - 1) * (q - 1)
    e = find_e(fi)
    
    # x*y == 1 mod p
    # y = pow(x, -1, p) for python 3.8+
    d = pow(e, -1, fi)
    
    return p, q, n, fi, e, d

def rsa_enc_str(m, n, e):
    return pow(m, e, n)

def rsa_dec_str(c, n, d):
    return pow(c, d, n)

def text_to_num(str):
    num = 0
    i = 0
    for ch in str:
        num = num * 100
        num = num + (ord(ch) - 87)
        i += 1
    return num

def num_to_text(num):
    text = ""
    temp = num
    while(temp > 0):
        text = chr((num % 100) + 87) + text
        temp = temp / 100
    return text

key_len = 128
p, q, n, fi, e, d = rsa_set(key_len)

plain_text = 123456789
print("plain= ", plain_text)
cyphertext = rsa_enc_str(plain_text, n, e)
print("cypher= ", cyphertext)
plaintext = rsa_dec_str(cyphertext, n, d)
print("plain= ", plaintext)