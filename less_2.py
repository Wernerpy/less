

p = 100
def pad():
    s=5
    e=6
    q=8
    print(p,s,e,q)

pad()

print(p)



def ploschad_prymougoln(a,b):
   return a*b

def podschet_monet(monety,ves,nomer):
    print("Всего вес монеты: %s " % nomer)
    print("Всего вес монеты: %s " % (monety * ves))

podschet_monet(20,2.3,1)

podschet_monet(200,2.3,2)

a1 = 180
b1 = 200

print("площадь прямоугольника %s на %s равно %s" % (a1,b1,ploschad_prymougoln(a1,b1) ))

for i in range(0,5):
    print("Введите число")
    a=int(input())
    print("Введите число")
    b=int(input())
    print("площадь прямоугольника %s на %s равно %s" % (a,b,ploschad_prymougoln(a,b) ))
 
