from math import gcd as gcd
#Ask user for p and q
p = 11
q = 13
n = p*q 

#Message length
message = 9

##Totient function
phi = (p-1)*(q-1) 

#Public key
e = 7

#Check if public key is co-prime to phi 
while e < phi:
    if gcd(e,phi) == 1:
        break
    else:
        e += 1

#Ensure d*e is = 1 mod phi
d = 1 / e
decrypt = d % phi

#Encrypting message
c = pow(message,e)

#Decrypting message
m = pow(c,decrypt)
m %= n
c %= n

#Print original message length, encrypted, and decrypted messages
print(message)
print(c)
print(round(m))
