
import turtle
p1 = turtle.Pen()
p2 = turtle.Pen()

p1.forward(200)
p2.left(90)
p2.forward(200)

class less:
    def funprt(self):
        print("Hello World")
        
class less1(less):
    pass

class less2(less):
    def __init__(self, price):
        self.my_price = price
    def read_price(self):
        print("my price %s" % self.my_price )
    def write_price(self, new_price):
        self.my_price = new_price
    def kto_ya(self):
        print("ученик")
    


obj = less2(200)
obj.kto_ya()
obj.funprt()
obj.read_price()
obj.write_price(500)
obj.read_price()

obj2 = less2(700)
obj2.read_price()

print(int(input()))