class voicebank:
    def __init__(self):
        self.__maxprice = 200
    def sell(self):
        print("selling price: {}".format(self.__maxprice))
    def setmaxprice(self, price):
        self.__maxprice = price
v4x = voicebank()
v4x.sell()
v4x.__maxprice = 400
v4x.sell()
v4x.setmaxprice(400)
v4x.sell()