from art import logo

print(logo)

bid = {}
biding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid_count = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid_count:
            highest_bid_count = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of: {highest_bid_count}")


while not biding_finished:
    name = input("What is your name?: ")
    price = int(input("What do you bid?: $"))
    bid[name] = price
    should_continue = input("Is there any other bidders? yes or no? ")
    if should_continue == "no":
        biding_finished = True
        find_highest_bidder(bid)
    elif should_continue == "yes":
        print("continue")
