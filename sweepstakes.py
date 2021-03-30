import random

contestants = {
    "player1": "sam samson",
    "player2": "john johnson",
    "player3": "turk turkleton",
    "player4": "peter peterson",
    "player5": "tim timson"
}
key_list = list(contestants.keys())
val_list = list(contestants.values())

def pick_winner():
    random_entry = random.choice(list(val_list))
    print(f' The winner is {random_entry}')

