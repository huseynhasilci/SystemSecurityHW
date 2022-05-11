from random import randint
from Crypto.Util import number
a_number = number.getPrime(256)
a_number_2 = number.getPrime(256)
# print(a_number_2)
# print(a_number)
# Both the persons will be agreed upon the
# public keys G and P
# A prime number P is taken
P = a_number
# A primitive root for P, G is taken
G = a_number_2
# Alice will choose the private key a
a = 61
# gets the generated key
x = int(pow(G, a, P))
# Bob will choose the private key b
b = 52
# gets the generated key
y = int(pow(G, b, P))
# Secret key for Alice
ka = int(pow(y, a, P))
# Secret key for Bob
kb = int(pow(x, b, P))
print('Kb+: ')
print(P)
print('Kb-: ')
print(a)
print('Kc+: ')
print(G)
print('Kc-: ')
print(b)
print('k3 : %d' % (ka))
print('Value for checking correctness : %d' % (kb))
print(f'Is symmetric keys are equal?: {ka == kb}')
