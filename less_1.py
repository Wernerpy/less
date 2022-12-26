#datetime https://docs.python.org/3/library/datetime.html

'''
import datetime
#print(datetime.datetime.today())
#print(datetime.datetime.now())
d1 = datetime.datetime.today()
print(d1)
d2 = d1+datetime.timedelta(seconds=1)
print(d2)
d3 = d1+datetime.timedelta(seconds=10)
print(d3)
print(d3-d2)
print((d3-d2).seconds)

print(d1.strftime("%a %A %w %d %b %X %x"))
print(d1.strftime("%X %x %c"))
print(d3.strftime("%c"))

'''
'''
#import modle_1
#print(modle_1.my_var)
#modle_1.my_function()

from modle_1 import *
print(my_var)
my_function()
'''

def podsche_monet_ves(monety , ves, nomer):
    print("всего вес монет: %s" % (monety * ves))
    print("Подсчет номер № %s" % nomer)


podsche_monet_ves(100, 2.5, 1)

podsche_monet_ves(200, 2.5, 2)
j = 20
for i in range(0,50):
    print(i,j,sep="***",end=" ")
