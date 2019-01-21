# from uuid import uuid4

from blockchain import Blockchain
from utility.verification import Verification
from wallet import Wallet


class Node:
    """The node which runs the local blockchain instance.
    :argument:id: The id of the node.
    :argument:blockchain: The blockchain which is run by this node.
    """

    def __init__(self):
        """The constructor of the Node class."""
        # self.wallet.public_key = str(uuid4())
        self.wallet = Wallet()
        self.wallet.create_keys()
        self.blockchain = Blockchain(self.wallet.public_key)

    @staticmethod
    def get_transaction_value():
        """
        :return: the input of the user (a new transaction amount) as a float.
        """
        # Get the user input, transform it from a string to a float and store it in user_input
        tx_recipient = input("Enter the recipient of the transaction: ")
        tx_amount = float(input("Your transaction amount please: "))
        return tx_recipient, tx_amount

    @staticmethod
    def get_user_choice():
        """ Prompts the user for its choice and return it. """
        user_input = input("Your choice: ")
        return user_input

    def print_blockchain_elements(self):
        """ Output all blocks of the blockchain. """
        # Output the blockchain list to the console
        for block in self.blockchain.chain:
            print("Outputting Block")
            print(block)
        else:
            print("-" * 20)

    def listen_for_input(self):
        waiting_for_input = True

        # A while loop for the user input interface
        # It's a loop that exits once waiting_for_input becomes False or when break is called
        while waiting_for_input:
            print("Please choose:")
            print("1: Add a new transaction value")
            print("2: Mine a new block")
            print("3: Output the blockchain blocks")
            print("4: Check transaction validity")
            print("5: Create wallet")
            print("6: Load wallet")
            print("7: Save wallet keys")
            print("q: Quit")
            user_choice = self.get_user_choice()
            if "1" == user_choice:
                tx_data = self.get_transaction_value()
                recipient, amount = tx_data
                # Add the transaction amount to the blockchain
                signature = self.wallet.sign_transaction(self.wallet.public_key, recipient, amount)
                if self.blockchain.add_transaction(recipient, self.wallet.public_key, signature, amount=amount):
                    print("Added transaction!")
                else:
                    print("Transaction failed!")
                print(self.blockchain.get_open_transactions())
            elif "2" == user_choice:
                if not self.blockchain.mine_block():
                    print("Mining failed. Got no wallet?")
            elif "3" == user_choice:
                self.print_blockchain_elements()
            elif "4" == user_choice:
                if Verification.verify_transactions(self.blockchain.get_open_transactions(),
                                                    self.blockchain.get_balance):
                    print("All transactions are valid")
                else:
                    print("There are invalid transactions")
            elif "5" == user_choice:
                self.wallet.create_keys()
                self.blockchain = Blockchain(self.wallet.public_key)
            elif "6" == user_choice:
                self.wallet.load_key()
                self.blockchain = Blockchain(self.wallet.public_key)
            elif "7" == user_choice:
                self.wallet.save_keys()
            elif "q" == user_choice:
                # This will lead to the loop to exist because it's running condition becomes False
                waiting_for_input = False
            else:
                print("Input was invalid, please pick a value from the list!")
            if not Verification.verify_chain(self.blockchain.chain):
                self.print_blockchain_elements()
                print("Invalid blockchain!")
                # Break out of the loop
                break
            print("Balance of '{}': {:6.2f}".format(self.wallet.public_key, self.blockchain.get_balance()))
        else:
            print("User left!")

        print("Done!")


if __name__ == "__main__":
    node = Node()
    node.listen_for_input()
