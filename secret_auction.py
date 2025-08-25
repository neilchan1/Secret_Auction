import sys

def secure_input(prompt=""):
    """Let user see input while typing, but erase it after Enter is pressed."""
    value = input(prompt)

    # Move cursor up one line and clear it
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    sys.stdout.flush()
    return value

def get_bidder_input(name):
    """Prompt user for bidder's name and bid amount."""
    while True:
        try:
            bid_str = secure_input(f"Enter {name}'s bid: £")
            bid = float(bid_str)
            if bid < 0:
                print("Bid must be a positive number.")
                continue
            return bid
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def find_highest_bidders(bids):
    """Return the list of bidders who placed the highest bid."""
    if not bids:
        return []
    max_bid = max(bids.values())
    winners = [name for name, bid in bids.items() if bid == max_bid]
    return winners

def additional_bidders(bidding_finished):
    while True:
        additional_bidder = input("Are there more bidders? (yes/no): ").strip().lower()

        if additional_bidder in ['yes', 'no']:
            break
        else: 
            print("Invalid input. Please enter 'yes' or 'no'.")

    if additional_bidder == 'no':
        bidding_finished = True

    return bidding_finished

def tie_breaker(bidders, winners):
    print(f"\nThere is a tie between: {', '.join(winners)}")
    print("These bidders must bid again!\n")

    new_bids = {}
    for name in bidders:  # keep original order
        if name in winners:
            bid = get_bidder_input(name)
            new_bids[name] = bid
        else:
            new_bids[name] = bidders[name]  # carry over old bid

    bidders = new_bids
    winners = find_highest_bidders(bidders)

    return bidders, winners