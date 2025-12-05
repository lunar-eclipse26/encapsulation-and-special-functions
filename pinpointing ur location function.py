class point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
xcoordinates = int(input("give me ur x coordinates lil bro: "))
ycoordinates = int(input("give me ur y coordinates lil bro: "))
p1 = point(xcoordinates, ycoordinates)
print(p1)
print("hehhehehehehehehee thanks for ur location lil bro")