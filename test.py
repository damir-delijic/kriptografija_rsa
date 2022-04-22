import rsa

rsasystem = rsa.Rsa(1024)

plain = "riba ribi grize rep"
print(plain)
cypher = rsasystem.ENCRYPT_MESSAFE(plain)
print(cypher)
p = rsasystem.DECRYPT_MESSAGE(cypher)
print(p)

