import hashlib
import json


def hash_str_256(string):
    """ Create a SHA256 hash for a given input string.
    :argument: string: The string which should be hashed.
    """
    return hashlib.sha256(string).hexdigest()


def hash_block(block):
    """Hashes a block and returns a string representation of it.
    :argument:block: The block that should be hashed.
    """
    return hash_str_256(json.dumps(block, sort_keys=True).encode())
