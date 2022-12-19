class Auction:
    __ID = 0
    __auctionDetails = {}
    __biddersSet = set() 

    def __init__(self, bidder1_name, bidder2_name, bidder1_bid=1, bidder2_bid=1):
        self.__bidder1_name = bidder1_name
        self.__bidder2_name = bidder2_name
        self.__bidder1_bid = bidder1_bid
        self.__bidder2_bid = bidder2_bid

        type(self).__ID += 1
        self.__id = type(self).__ID 

        type(self).__biddersSet.update([bidder1_name, bidder2_name])
        
        # crate a dictionary with key as ID and value as a string with bidder1_name, bidder2_name, bidder1_bid, bidder2_bid
        type(self).__auctionDetails[type(self).__ID] = f"{self.__bidder1_name} ({self.__bidder1_bid}) :  {self.__bidder2_name} ({self.__bidder2_bid})"

    @classmethod
    def showDetailsfromID(cls, match_id):
        if match_id in cls.__auctionDetails.keys():
            print(cls.__auctionDetails[match_id])

    @classmethod
    def printBiddersList(cls):
        # teamList= sorted(list(cls.__biddersSet))
        # print(*teamList, sep=", ") # using * to unpack the list
        print(*sorted((cls.__biddersSet)), sep=", ") # using * to unpack the list
        
    @classmethod
    def isTie(cls, bids):
        bidder1_bid, bidder2_bid = bids
        return bidder1_bid == bidder2_bid

    def __gt__(self, other):
        return (self.__bidder1_bid + self.__bidder2_bid) > (other.__bidder1_bid + other.__bidder2_bid)

    def __lt__(self, other):
        return (self.__bidder1_bid + self.__bidder2_bid) < (other.__bidder1_bid + other.__bidder2_bid)

    def __eq__(self, other):
        return (self.__bidder1_bid + self.__bidder2_bid) == (other.__bidder1_bid + other.__bidder2_bid)

    def getID(self):
        return self.__id

    def getBids(self):
        return (self.__bidder1_bid, self.__bidder2_bid)


bid1 = Auction("KKR", "CSK", 2 ,2)
bid2 = Auction("CSK", "MI", 0, 3)
Auction.printBiddersList() # prints sorted list of bidders
print("=====================================")
bid3 = Auction("RCB", "KKR")
bid4 = Auction("KKR", "MI", 2)
print(bid1 > bid2)
print(bid2 == bid1)
print(bid1.getID())
Auction.showDetailsfromID(3)
print("=====================================")
print(bid3 < bid4)
print(bid4 == bid3)
print(bid2.getBids())
print("=====================================")
print(Auction.isTie(bid3.getBids()))
print(Auction.isTie(bid4.getBids()))
Auction.printBiddersList() # prints sorted list of bidders
print("=====================================")
