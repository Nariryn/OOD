class BidAuction:
    def __init__(self, bid):
        self.bid = bid
        
    def winner(self):
        if len(self.bid) < 2:
            return "not enough bidder"
        
        sorted_bid = sorted(self.bid, reverse=True)
        
        if sorted_bid[0] == sorted_bid[1]:
            return "error : have more than one highest bid"
        
        highest_bid = sorted_bid[0]
        second_highest_bid = sorted_bid[1]
        
        return f"winner bid is {highest_bid} need to pay {second_highest_bid}"

bid = list(map(int, input("Enter All Bid : ").split()))

auction = BidAuction(bid)
result = auction.winner()

print(result)
