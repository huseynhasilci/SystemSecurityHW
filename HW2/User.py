from Crypto.PublicKey import RSA
from Crypto import Random


class User:
    def __init__(self, username):
        self.username = username
        self.__certificated_public_key = None
        self.__private_key = None
        self.__public_key = None

    def create_key_pair(self):
        key = RSA.generate(1024, Random.new().read)  # generating key with RSA
        self.__public_key = key.publickey().exportKey("PEM")
        self.__private_key = key.exportKey("PEM")
        """
        public_key = key.publickey().exportKey("PEM").decode()
        private_key = key.exportKey("PEM").decode()
        self.__private_key = private_key.split("-----")[2]
        public_key = public_key.split("-----")[2]
        """

    # getter - setter
    def set_certificated_public_key(self, signature):
        self.__certificated_public_key = signature

    def get_certificated_public_key(self):
        return self.__certificated_public_key

    def get_public_key(self):
        return self.__public_key

