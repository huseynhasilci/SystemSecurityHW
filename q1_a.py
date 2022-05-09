from Crypto.PublicKey import RSA
import pprint
key = RSA.generate(1024)
p_key = key.publickey().exportKey("PEM")
priv_key = key.exportKey("PEM")
pprint.pprint(p_key)
pprint.pprint(priv_key)
