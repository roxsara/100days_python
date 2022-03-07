import os
from art import logo

print(logo)

bidding = True
bids = {}

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def highest_bid(all_bids):
    max_bid = 0
    for bidder, bid in all_bids.items():
        if bid > max_bid:
            max_bidder = bidder
            max_bid = bid
    print(f"The winner is {max_bidder} with a bid of ${max_bid}. Congratulations!")


while bidding:
    name = input("Please enter your name ")
    price = float(input("Please enter your bid price $"))
    bids[name] = price
    more_bids = input("Are there any other bidders? y/n ")
    if more_bids == "n":
        bidding = False
        highest_bid(bids)
    else:
        clearConsole()