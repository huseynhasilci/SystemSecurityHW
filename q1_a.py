from Crypto.PublicKey import RSA
import pprint
key = RSA.generate(1024)  # genereting key with RSA
p_key = key.publickey().exportKey("PEM")  # exporting the public key from key we created
priv_key = key.exportKey("PEM")  # exporting the priv key from key we created
pprint.pprint(p_key)    # showing the public key
pprint.pprint(priv_key)  # showing the priv key
