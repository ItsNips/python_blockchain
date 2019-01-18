from collections import OrderedDict

from printable import Printable


class Transaction(Printable):
    """A transaction which can be added to a block in the blockchain.
    :argument: The sender of the coins.
    :argument: The recipient of the coins.
    :argument: The amount of coins sent.
    """
    def __init__(self, sender, recipient, amount):
        """The constructor of the Transaction class."""
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def to_ordered_dict(self):
        """Converts this transaction into a (hashable) OrderedDict."""
        return OrderedDict([("sender", self.sender), ("recipient", self.recipient), ("amount", self.amount)])
