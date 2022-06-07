import codecs

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Signature import pkcs1_15
import rsa



class CA:
    def __init__(self):
        self.__certificated_public_keys = {}  # key: username, value=signature
        self.__private_key = None
        self.__public_key = None
        self.create_key_pair()

    def create_key_pair(self):
        key = RSA.generate(1024, Random.new().read)  # generating key with RSA
        self.__public_key = key.publickey().exportKey("PEM")  # key object to string
        self.__private_key = key.exportKey("PEM")   # key object to string
        """
        public_key = key.publickey().exportKey("PEM").decode()
        private_key = key.exportKey("PEM").decode()
        self.__private_key = private_key.split("-----")[2]
        self.__public_key = public_key.split("-----")[2]
        """

    def certificate_public_key(self, username, public_key):
        private_key_obj = RSA.importKey(self.__private_key)  # string to key object
        digest = SHA256.new(public_key.decode().encode('utf-8'))
        signer = pkcs1_15.new(private_key_obj)
        signature = signer.sign(digest)
        self.__certificated_public_keys[username] = signature
        return signature

    def verify_public_key(self, signature, public_key):
        ca_public_key = RSA.importKey(self.__public_key)
        digest = SHA256.new(public_key.decode().encode('utf-8'))
        try:
            verifier = pkcs1_15.new(ca_public_key)
            verifier.verify(digest, signature)
            return public_key
        except:
            return False


