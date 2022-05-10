import pprint

from Crypto.Cipher import AES
from secrets import token_bytes

key = token_bytes(16)
k1 = '8bfiZitGPry4Tr/bPuneo+lch9q+Gl4ozao1v2Kp+p4Zh38CUCgKG0AQTwBFyPu9M1/Zl+TjLMxnqCAgfx7kNq74j5EJsjo1ACSm2906BYgzdoXr+yqDJNLMcBE42Evfsqsw10vq+KBR21ptYcGykgC0RH2qO/6L7rjJmmeqSN8='
k2 = 'A1TJ+BTSKf3Xo4sjNHCj8EHnsKWWP6zHZ7qZcZRy4BotH2Ci6dELIyork6l/Ejnzi3A3aFfiT6AObx+o9iudIgxkd7NtCz9S1G5Ql5CXrUHqKZH3x5vy0QMlvs6emcfajTSSs85EGyi3Q8EM6GoM4bVyZBLLLqXcNnJH9hwzJ5/Ay5QEuzmyBjgujvYppr0LxUmbF+S9CzkuuobgRGuiDF1koqMvD9bQIL181MGIbCP7yyhmo4kQoQJ0S9wQ8g+rHx2P7sBiMBXE7OKbUQiLNI33jnpTF4UvP4ICedDxGPzSgLmBWHGt4R7HOcw/gBzhqhm5EztoEzKrNmptx4Vl3g=='
# k_plus = """MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDCvvFeT0kEDYBDB/2DyoKZr6agPE2zsS4ckpxFiHAK4cM5B+dmQudwviXWTXAF6PfYQ44D5csDT3DQMgVvRPdt8VcGRyvm+Eg4G4WZU7psfuKyuB6quxLgpnAA/jAnRhPRlcksKObvIvvgalz2jMTAq7FX9iD5Sp/ZjB04xRnXLwIDAQAB"""
def encrypt(msg):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    k_plus, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    # print(ciphertext)
    return nonce, k_plus, tag


def decrypt(nonce, ciphertext, tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False


nonce_k1, ciphertext_k1, tag_k1 = encrypt(k1)
nonce_k2, ciphertext_k2, tag_k2 = encrypt(k2)
# nonce_kplus, ciphertext_kplus, tag_kplus = encrypt(k_plus)

plaintext_k1 = decrypt(nonce_k1, ciphertext_k1, tag_k1)
print(f'Cipher text: {ciphertext_k1}')
pprint.pprint(ciphertext_k1)
plaintext_k2 = decrypt(nonce_k2, ciphertext_k2, tag_k2)
print(f'Cipher text: {ciphertext_k2}')
pprint.pprint(ciphertext_k2)

#plaintext_kplus = decrypt(nonce_kplus, ciphertext_kplus, tag_kplus)
# print(f'Cipher text: {ciphertext_kplus}')
print('********************** k1 **********************')
pprint.pprint(plaintext_k1)
print('********************** k2 **********************')
pprint.pprint(plaintext_k2)

"""if not plaintext:
    print('Message is corrupted')
else:
    print(f'Plain text: {plaintext}')"""
