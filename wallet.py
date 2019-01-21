from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import PKCS1_v1_5
from Cryptodome.Hash import SHA3_256
import Cryptodome.Random
import binascii


class Wallet:
    def __init__(self):
        self.private_key = None
        self.public_key = None

    def create_keys(self):
        private_key, public_key = self.generate_keys()
        self.private_key = private_key
        self.public_key = public_key

    def save_keys(self):
        if self.public_key is not None and self.private_key is not None:
            try:
                with open("resources/wallet.txt", mode="w") as f:
                    f.write(self.public_key)
                    f.write("\n")
                    f.write(self.private_key)
            except (IOError, IndexError):
                print("Saving wallet failed...")

    def load_key(self):
        try:
            with open("resources/wallet.txt", mode="r") as f:
                keys = f.readlines()
                public_key = keys[0][:-1]
                private_key = keys[1]
                self.private_key = private_key
                self.public_key = public_key
        except (IOError, IndexError):
            print("Loading wallet failed...")

    @staticmethod
    def generate_keys():
        private_key = RSA.generate(1024, Cryptodome.Random.new().read)
        public_key = private_key.publickey()
        return (binascii.hexlify(private_key.exportKey(format="DER")).decode("ascii"),
                binascii.hexlify(public_key.publickey().exportKey(format="DER")).decode("ascii"))

    def sign_transaction(self, sender, recipient, amount):
        signer = PKCS1_v1_5.new(RSA.import_key(binascii.unhexlify(self.private_key)))
        hash_f = SHA3_256.new((str(sender) + str(recipient) + str(amount)).encode("utf8"))
        signature = signer.sign(hash_f)
        return binascii.hexlify(signature).decode("ascii")
