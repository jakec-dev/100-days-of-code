from os import system
from art import logo

def clear():
    system("clear")

print(logo)
print("Welcome to the secret auction program.")

bidding_finished = False
all_bids = {}

while not bidding_finished:
    name = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: $"))
    add_another_bid = input("Are there any other bidders? Type 'yes' or 'no.\n").lower()
    all_bids[name] = bid_amount
    if add_another_bid == "no":
        top_bid = 0
        top_bidder = ""
        for name in all_bids:
            bid_amount = all_bids[name]
            if bid_amount > top_bid:
                top_bid = bid_amount
                top_bidder = name
        print(f"{top_bidder} wins the auction for ${top_bid}")
        bidding_finished = True
    else:
        clear()
