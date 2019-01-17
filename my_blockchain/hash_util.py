import hashlib
import json


def hash_str_256(string):
    return hashlib.sha256(string).hexdigest()


def hash_block(block):
    """ Hashes a block.
    :argument: block: The block that should be hashed.
    :return: a string representation of hashes a block
    """
    return hash_str_256(json.dumps(block, sort_keys=True).encode())
