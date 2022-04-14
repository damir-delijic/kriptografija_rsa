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

def rsa_enc_text(text, n, e):
    limit = 100
    encrypted_text = rsa_enc_str(text[0:limit], n, e)
    while limit < len(text):
        limit += 100
        encrypted_text += rsa_enc_str(text[limit-100 : limit], n, e)
    return encrypted_text

# def rsa_dec_text(num, n, d):
#     decrypted_text = rsa_dec_str(text[0:limit], n, d)
#     while limit < len(text):
#         limit += 100
#         decrypted_text += rsa_dec_str(text[limit-100 : limit], n, d)
#     return decrypted_text

def rsa_enc_str(str, n, e):
    m = text_to_num(str)
    return pow(m, e, n)

def rsa_dec_str(c, n, d):
    m = pow(c, d, n)
    return num_to_text(m)

def text_to_num(str):
    num = 0
    for ch in str:
        num = num * 1000
        num = num + (ord(ch) + 100)
    return num

def num_to_text(num):
    text = ""
    while(num > 0):
        text = chr((num % 1000) - 100) + text
        num = num // 1000
    return text
# flaw koristi 3 decimalne cifre da kodira oko 150 vrijednosti, tri binarne cifre vise nego sto treba, ali ko ga jebe
key_len = 512
p, q, n, fi, e, d = rsa_set(key_len)

plaintext = "network content network content network content network content network content network content networ"
encrypted = rsa_enc_text(plaintext, n, e)
print("encrypted= ", encrypted)
decrypted = rsa_dec_text(encrypted, n, d)
print("decrypted= ", decrypted)
