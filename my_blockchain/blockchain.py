# Initializing our (empty) blockchain list
blockchain = []


def get_last_blockchain_value():
    """
    :return: the last value of the current blockchain.
    """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


# This function accepts two arguments.
# One required one (transaction_amount) and one optional one (last_transaction)
# The optional one is optional because it has a default value => [1]
def add_transaction(transaction_amount, last_transaction=None):
    """ Append a new value as well as the last blockchain value to the blockchain.
    :argument transaction_amount: The amount that should be added
    :argument last_transaction: The last blockchain transaction (default=[1])
    """
    if last_transaction is None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """
    :return: the input of the user (a new transaction amount) as a float.
    """
    # Get the user input, transform it from a string to a float and store it
    user_input = float(input("Your transaction amount please: "))
    return user_input


def get_user_choice():
    user_input = input("Your choice: ")
    return user_input


def print_blockchain_elements():
    # Output the blockchain list to the console
    for block in blockchain:
        print("Outputting Block")
        print(block)


def verify_chain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        if block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid


while True:
    print("Please choose:")
    print("1: Add a new transaction value")
    print("2: Output the blockchain blocks")
    print("h: Manipulate the chain")
    print("q: Quit")
    user_choice = get_user_choice()
    if "1" == user_choice:
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif "2" == user_choice:
        print_blockchain_elements()
    elif "h" == user_choice:
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif "q" == user_choice:
        break
    else:
        print("Input was invalid, please pick a value from the list!")
    if not verify_chain():
        print("Invalid blockchain!")
        break

print("Done!")
