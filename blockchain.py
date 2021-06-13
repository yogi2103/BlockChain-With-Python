# Initializing our (empty) blockchain list
genesis_block={
    'previous_hash': '', 
    'index':0,
    'transactionns':[]
}
blockchain = [genesis_block]
open_transactions=[]
owner='Max'

def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

# This function accepts two arguments.
# One required one (transaction_amount) and one optional one (last_transaction)
# The optional one is optional because it has a default value => [1]


def add_transaction(recepient,sender=owner,amount=1.0):
    """ Append a new value as well as the last blockchain value to the blockchain.

    Arguments:
        :Sender : Sender of the coins
        :recepient: recepient of the coins
        :amount: amount of coins sent with the transaction (default=1.0)
    """
    transaction={
        'sender': sender, 
        'recepient':recepient,
        'amount':amount
        }
    open_transactions.append(transaction)
    


def mine_block():
    last_block=blockchain[-1]
    hashed_block='-'.join([str(last_block[key]) for key in last_block])
    print(hashed_block)
    block={
        'previous_hash': hashed_block, 
        'index':len(blockchain),
        'transactionns':open_transactions
    }
    blockchain.append(block)
    pass

def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float. """
    # Get the user input, transform it from a string to a float and store it in user_input
    tx_recepient= input('Enter the recepient\'s name')
    tx_amount = float(input('Your transaction amount please: '))
    return (tx_recepient,tx_amount)


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    # Output the blockchain list to the console
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print('_'*20)


def verify_chain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        elif block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid

waiting_for_input= True
while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new Block')
    print('3: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recepient, amount= tx_data
        add_transaction(recepient,amount=amount)
        print(open_transactions)
    elif user_choice=='2':
        mine_block()
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input= False
    else:
        print('Input was invalid, please pick a value from the list!')
    # if not verify_chain():
    #     print('Invalid blockchain!')
    #     break

else:
    print('User left')

print('Done!')
