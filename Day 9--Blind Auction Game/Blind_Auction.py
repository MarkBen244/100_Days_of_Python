print("welcome to Marks Silent Auction!")

name_and_bids = {}


def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    max(bidding_dictionary)

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")


marking = True
while marking == True:
    name1 = input("Whats your name? ").lower()
    bid1 = int(input("What's your bid?  $"))
    name_and_bids[name1] = bid1
    additional_players = input(
        "Are there more players? Type 'yes' or 'no'? ").lower()
    if additional_players == "no":
        marking = False
        find_highest_bidder(name_and_bids)
    elif additional_players == "yes":
        print("\n"*5)
