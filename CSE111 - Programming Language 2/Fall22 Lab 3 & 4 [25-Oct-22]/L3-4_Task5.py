class KhabarKoi:
    def __init__(self, name, phone, address):
        self.name= name
        self.phone= phone
        self.address= address
        self.token = self.name[0:3] + self.phone[3:6] + self.address[0:3]

        self.itemList= []
        self.orderDict = {}
        self.deliveryCharge = 30

        print(f"{self.name}, welcome to KhabarKoi! Your token number is {self.token}")

    def add_items(self, *items):
        self.itemList = list(items)
        half_order_length = len(self.itemList)//2
        for i in range(half_order_length):
            self.orderDict[self.itemList[i]] = self.itemList[i+half_order_length]

        # for item in items:
        #     if isinstance(item, str):
        #         self.itemList.append(item)
        #     else:
        #         self.priceList.append(item)
        # self.orderDict = dict(zip(self.itemList, self.priceList))

    def print_order_detail(self):
        print(f"Customer Details: Name: {self.name}, Phone: {self.phone}, Address: {self.address}\nOrders:{self.orderDict}\nPaid: {sum(self.orderDict.values()) + self.deliveryCharge} Tk")

    def place_order(self, token):
        if token == self.token:
            print(f"Order placed successfully.")
            self.print_order_detail()
        else:
            print("xxx Invalid token number xxx")



order1 = KhabarKoi("Shakib", "01756918xxx", "Mohakhali")
order1.add_items("Burger", "Coca Cola", 220, 50)
print("-------------------")
order1.place_order("Sha017Moh")
print("-------------------")
order1.place_order("Sha569Moh")

print("=========================")
order2 = KhabarKoi("Siam", "01719659xxx", "Uttara")
order2.add_items("Pineapple", "Dairy Milk", "Pizza", "Fries", 100, 50, 500, 95)
print("-------------------")
order2.place_order("Sia196Utt")
print("=========================")
