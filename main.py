import secret_auction
from ascii_art import GAVEL, INTRO

def main():
    print(INTRO)
    print("Welcome to the Secret Auction!")

    bidders = {}
    bidding_finished = False

    # Collect initial bids
    while not bidding_finished:
        name = input("Enter bidder's name: ").strip()
        bid = secret_auction.get_bidder_input(name)
        bidders[name] = bid

        bidding_finished = secret_auction.additional_bidders(bidding_finished)

    # Determine winner(s)
    winners = secret_auction.find_highest_bidders(bidders)

    # Handle ties
    while len(winners) > 1:
        bidders, winners = secret_auction.tie_breaker(bidders, winners)

    # Announce winner
    winner = winners[0]
    print(GAVEL)
    print(f"\nThe winner is {winner} with a bid of £{bidders[winner]:.2f}!")

if __name__ == "__main__":
    main()