
from tabnanny import check
from tkinter import *
#from cmath import *
from math import *
import re
from functools import partial


def label_all():

    lb1 = Label(text=' Вычисление внутреннего диаметра кольца ',font='Arial 13 bold', bg = '#999')
    lb1.place(x=200,y=5)
    

    lb2 = Label(text='Внешний диаметр D 1',bg='#999')
    lb2.place(x=5,y=50)

    lb222 = Label(text='Внешний диаметр D 2',bg='#999')
    lb222.place(x=405,y=50)

    lb233 = Label(text='Внешний диаметр D 3',bg='#999')
    lb233.place(x=605,y=50)

    lb233 = Label(text='Внешний диаметр D 4',bg='#999')
    lb233.place(x=805,y=50)


    lb7 = Label(text=' Внутренний диаметр d: ',bg='#999')
    lb7.place(x=10,y=310)
    '''
    lb722 = Label(text=' Внутренний диаметр d: ',bg='#999')
    lb722.place(x=410,y=310)

    lb733 = Label(text=' Внутренний диаметр d: ',bg='#999')
    lb733.place(x=610,y=310)

    lb733 = Label(text=' Внутренний диаметр d: ',bg='#999')
    lb733.place(x=810,y=310)
    '''

    lb3 = Label(text='Высота H',bg='#999')
    lb3.place(x=5, y=100)

    lb322 = Label(text='Высота H',bg='#999')
    lb322.place(x=405, y=100)

    lb333 = Label(text='Высота H',bg='#999')
    lb333.place(x=605, y=100)

    lb333 = Label(text='Высота H',bg='#999')
    lb333.place(x=805, y=100)


    lb4 = Label(text='Масса m', bg='#999')
    lb4.place(x=5,y=150)

    lb422 = Label(text='Масса m', bg='#999')
    lb422.place(x=405,y=150)

    lb433 = Label(text='Масса m', bg='#999')
    lb433.place(x=605,y=150)

    lb433 = Label(text='Масса m', bg='#999')
    lb433.place(x=805,y=150)


    lb5 = Label(text='Плотность p 1',bg='#999')
    lb5.place(x=5,y=200)

    lb522 = Label(text='Плотность p 2',bg='#999')
    lb522.place(x=405,y=200)

    lb533 = Label(text='Плотность p 3',bg='#999')
    lb533.place(x=605,y=200)

    lb533 = Label(text='Плотность p 4',bg='#999')
    lb533.place(x=805,y=200)



    lb8 = Label(text='Внешний диаметр D ',bg='#777')
    lb8.place(x=205,y=50)

    lb9 = Label(text='Высота H',bg='#777')
    lb9.place(x=205, y=100)

    lb10 = Label(text='Внутренний диаметр d', bg='#777')
    lb10.place(x=205,y=150)

    lb11 = Label(text='Плотность p',bg='#777')
    lb11.place(x=205,y=200)

    lb27 = Label(text=' Ответ ',bg='#777')
    lb27.place(x=200,y=310)

def ent_all():


    en1D = Entry(validate='key', validatecommand=check, textvariable=number1)
    en1D.place(x=5,y=70)

    en2H = Entry(validate='key', validatecommand=check, textvariable=number2)
    en2H.place(x=5,y=120)

    en3m = Entry(validate='key', validatecommand=check, textvariable=number3)
    en3m.place(x=5,y=170)

    en4p = Entry(validate='key', validatecommand=check,textvariable=number4)
    en4p.place(x=5,y=220)



 

    en2H = Entry(validate='key', validatecommand=check, textvariable=number2)
    en2H.place(x=405,y=120)

    en3m = Entry(validate='key', validatecommand=check, textvariable=number3)
    en3m.place(x=405,y=170)

    en1D22 = Entry(validate='key', validatecommand=check, textvariable=number12)
    en1D22.place(x=405,y=70)

    en4p2211 = Entry(validate='key', validatecommand=check,textvariable=number11)
    en4p2211.insert(0,1)
    en4p2211.place(x=405,y=220)




    en1D22 = Entry(validate='key', validatecommand=check, textvariable=number13)
    en1D22.place(x=605,y=70)

    en2H = Entry(validate='key', validatecommand=check, textvariable=number2)
    en2H.place(x=605,y=120)

    en3m = Entry(validate='key', validatecommand=check, textvariable=number3)
    en3m.place(x=605,y=170)



    en4p2210 = Entry(validate='key', validatecommand=check,textvariable=number10)
    en4p2210.insert(0,1)
    en4p2210.place(x=605,y=220)

    

    en1D22 = Entry(validate='key', validatecommand=check, textvariable=number14)
    en1D22.place(x=805,y=70)

    en2H = Entry(validate='key', validatecommand=check, textvariable=number2)
    en2H.place(x=805,y=120)

    en3m = Entry(validate='key', validatecommand=check, textvariable=number3)
    en3m.place(x=805,y=170)



    en4p229 = Entry(validate='key', validatecommand=check,textvariable=number9)
    en4p229.insert(0,1)
    en4p229.place(x=805,y=220)



    en5D = Entry(validate='key', validatecommand=check, textvariable=number5)
    en5D.place(x=205,y=70)

    en6H = Entry(validate='key', validatecommand=check, textvariable=number6)
    en6H.place(x=205,y=120)

    en7d = Entry(validate='key', validatecommand=check, textvariable=number7)
    en7d.place(x=205,y=170)

    en8p = Entry(validate='key', validatecommand=check,textvariable=number8)
    en8p.place(x=205,y=220)

def is_valid(newval):
    return re.match("\\d{0,11}", newval) is not None

def clears():

    lb26.config(text=' D: ')
    lb27.config(text=' d: ')
    lb6.config(text=' ....  ',bg='#999')
    lb6.place(x=15,y=330) 
    Label(text="                                                                                                                                         " ,bg='#999').place(x=500,y=310)
            

    en1D = Entry(validate='key', validatecommand=check, textvariable=number1)
    en1D.delete(0,END)
    en1D.place(x=5,y=70)
    en2H = Entry(validate='key', validatecommand=check, textvariable=number2)
    en2H.place(x=5,y=120)
    en2H.delete(0,END)
    en3m = Entry(validate='key', validatecommand=check, textvariable=number3)
    en3m.place(x=5,y=170)
    en3m.delete(0,END)
    en4p = Entry(validate='key', validatecommand=check,textvariable=number4)
    en4p.place(x=5,y=220)
    en4p.delete(0,END)
    en2H = Entry(validate='key', validatecommand=check, textvariable=number2)
    en2H.place(x=405,y=120)
    en2H.delete(0,END)
    en3m = Entry(validate='key', validatecommand=check, textvariable=number3)
    en3m.place(x=405,y=170)
    en3m.delete(0,END)
    en1D22 = Entry(validate='key', validatecommand=check, textvariable=number12)
    en1D22.place(x=405,y=70)
    en1D22.delete(0,END)
    en4p2211 = Entry(validate='key', validatecommand=check,textvariable=number11)
    en4p2211.delete(0,END)
    en4p2211.place(x=405,y=220)
    en1D22 = Entry(validate='key', validatecommand=check, textvariable=number13)
    en1D22.place(x=605,y=70)
    en1D22.delete(0,END)
    en2H = Entry(validate='key', validatecommand=check, textvariable=number2)
    en2H.place(x=605,y=120)
    en2H.delete(0,END)
    en3m = Entry(validate='key', validatecommand=check, textvariable=number3)
    en3m.place(x=605,y=170)
    en3m.delete(0,END)
    en4p2210 = Entry(validate='key', validatecommand=check,textvariable=number10)
    en4p2210.delete(0,END)
    en4p2210.place(x=605,y=220)
    en1D22 = Entry(validate='key', validatecommand=check, textvariable=number14)
    en1D22.place(x=805,y=70)
    en1D22.delete(0,END)
    en2H = Entry(validate='key', validatecommand=check, textvariable=number2)
    en2H.place(x=805,y=120)
    en2H.delete(0,END)
    en3m = Entry(validate='key', validatecommand=check, textvariable=number3)
    en3m.place(x=805,y=170)
    en3m.delete(0,END)
    en4p229 = Entry(validate='key', validatecommand=check,textvariable=number9)
    en4p229.delete(0,END)
    en4p229.place(x=805,y=220)
    en5D = Entry(validate='key', validatecommand=check, textvariable=number5)
    en5D.place(x=205,y=70)
    en5D.delete(0,END)
    en6H = Entry(validate='key', validatecommand=check, textvariable=number6)
    en6H.place(x=205,y=120)
    en6H.delete(0,END)
    en7d = Entry(validate='key', validatecommand=check, textvariable=number7)
    en7d.place(x=205,y=170)
    en7d.delete(0,END)
    en8p = Entry(validate='key', validatecommand=check,textvariable=number8)
    en8p.place(x=205,y=220)
    en8p.delete(0,END)


def show(lb6,en1D,en2H,en3m,en4p,en4p229,en4p2210,en4p2211):
    D = (en1D.get())
    H = (en2H.get())
    m = (en3m.get())
    p = (en4p.get())
    p9 = (en4p229.get())
    p10 = (en4p2210.get())
    p11 = (en4p2211.get())

    try:

        D = float(D)
        m = float(m)
        p = float(p)
        p9 = float(p9)
        p10 = float(p10)
        H = float(H)

    except ValueError:
        print("ValueError: could not convert string to float:")


    print('D',D)
    print('m',m)
    print('p',p)
    print('H',H)

    try:

        #D = 100
        #m = 46.22
        m = round(m,2)
        #H = 1
        pi = 3.1415 
        #p = 7.85 
        V = m/p*1000
        V = round(V,2)
        S = V / H
        S = round(S,2)
        x = V * m / p * H 
        S2 = (pi * D**2 / 4) - S 
        S3 = S2/pi*4
        
        if S3 < 0:
            Label(text="Отрицательный корень %s" % S3,bg='red').place(x=500,y=310)
            print(S3)

        S4 = sqrt(S3)
        S4 = round(S4,2)
        print('')
        print('Result D:',D)
        print('Result d:',S4)
        print('Result H:',H)
        print('Result V:',V)
        print('Result m:',m)
        print('Result S:',S)

        print('')

        #1

        en1D22 = Entry(validate='key', validatecommand=check, textvariable=number12)
        en1D22.delete(0,END)
        en1D22.insert(0,S4)
        en1D22.place(x=405,y=70)

        m = round(m,2)
        pi = 3.1415 
        V = m/p9*1000
        V = round(V,2)
        S = V / H
        S = round(S,2)
        x = V * m / p9 * H 
        S2 = (pi * S4**2 / 4) - S 
        S3 = S2/pi*4

        if S3 < 0:
            Label(text="Отрицательный корень %s" % S3,bg='red').place(x=500,y=310)
            print(S3)

        S5 = sqrt(S3)
        S5 = round(S5,2)

        #2

        en1D22 = Entry(validate='key', validatecommand=check, textvariable=number13)
        en1D22.delete(0,END)
        en1D22.insert(0,S5)
        en1D22.place(x=605,y=70)

        m = round(m,2)
        pi = 3.1415 
        V = m/p10*1000
        V = round(V,2)
        S = V / H
        S = round(S,2)
        x = V * m / p10 * H 
        S2 = (pi * S5**2 / 4) - S 
        S3 = S2/pi*4

        if S3 < 0:
            Label(text="Отрицательный корень %s" % S3,bg='red').place(x=500,y=310)
            print(S3)

        S6 = sqrt(S3)
        S6 = round(S6,2)

        #3

        en1D22 = Entry(validate='key', validatecommand=check, textvariable=number14)
        en1D22.delete(0,END)
        en1D22.insert(0,S6)
        en1D22.place(x=805,y=70)

        lb6['text'] = S4 ,'mm'
        return
        
    except TypeError:

        en1D = Entry(validate='key', validatecommand=check, textvariable=number1)
        en1D.delete(0,END)
        en1D.insert(0,"Введите данные!!!")
        en2H = Entry(validate='key', validatecommand=check, textvariable=number2)
        en2H.delete(0,END)
        en2H.insert(0,"Введите данные!!!")
        en3m = Entry(validate='key', validatecommand=check, textvariable=number3)
        en3m.delete(0,END)
        en3m.insert(0,"Введите данные!!!")
        en4p = Entry(validate='key', validatecommand=check,textvariable=number4)
        en4p.delete(0,END)
        en4p.insert(0,"Введите данные!!!")
        
        print("TypeError: Введите данные!!! ValueError: could not convert string to float:")    

def show1(lb26,en5D,en6H,en7d,en8p):

    D = (en5D.get())
    H = (en6H.get())
    d = (en7d.get())
    p = (en8p.get())

    try:

        D = float(D)
        d = float(d)
        p = float(p)
        H = float(H)

    except ValueError:
        
        print("ValueError: could 314not convert string to float:")

        print('D',D)
        print('d',d)
        print('p',p)
        print('H',H)

    try:

        pi = float(3.14) #постоянная величина
        T = float(D - d)/2 #толщина

        m = float(pi * H * T * (d + T) / 1000 * p) #масса
        m = round(m,2)

        V1 = H * T * pi * (d + T) #объем
        V1 = round(V1,2)
        V2 = m/p #объем

        S = pi / 4 * ((d + 2 * T)**2 - d**2) #площадь
        S1 = pi / 4 * (D**2 - (D - 2 * T)**2) #площадь
        S2 = pi / 4 * (D**2 - d**2) #площадь
        S2 = round(S2,2)

        C1 = pi * D #длина окружности
        C2 = pi * (D - T)
        C3 = pi * (d + T)


        print(' ')

        print('Result D:',D)
        print('Result m:',m)
        print('Result H:',H)
        print('Result d:',d)
        print('Result V1:',V1)
        print('Result S2:',S2)

        print(' ')

        #lb26['text'] = 'D:',D,  'm:',m,' \n  H:',H,'d:',d,'V1:',V1,'S2:',S2
        #return
        lb26.config(text=' D: '+str(D)+' m: '+str(m)+' H; '+str(H))
        lb27.config(text=' d: '+str(d)+' V: '+str(V1)+' S: '+str(S2))

    except TypeError:
        en5D = Entry(validate='key', validatecommand=check, textvariable=number5)
        en5D.delete(0,END)
        en5D.insert(0,"Введите данные!!!")

        en6H = Entry(validate='key', validatecommand=check, textvariable=number6)
        en6H.delete(0,END)
        en6H.insert(0,"Введите данные!!!")

        en7d = Entry(validate='key', validatecommand=check, textvariable=number7)
        en7d.delete(0,END)
        en7d.insert(0,"Введите данные!!!")

        en8p = Entry(validate='key', validatecommand=check,textvariable=number8)
        en8p.delete(0,END)
        en8p.insert(0,"Введите данные!!!")

        print("TypeError: Введите данные!!! ValueError: could not convert string to float:")    

root = Tk()
root.title('Площадь')
root.geometry('1000x400+10+10')
root.resizable(0,0)
root['bg']= '#999'

lb6 = Label(text=' ....  ',bg='#999')
lb6.place(x=15,y=330) 

lb26 = Label(text=' .... ',bg='#999')
lb26.place(x=205,y=330) 

lb27 = Label(text=' .... ',bg='#999')
lb27.place(x=205,y=360) 

number1 = StringVar()
number2 = StringVar()  
number3 = StringVar()
number4 = StringVar()
number5 = StringVar()
number6 = StringVar()  
number7 = StringVar()
number8 = StringVar()
number9 = StringVar()
number10 = StringVar()
number11 = StringVar()
number12 = StringVar()
number13 = StringVar()
number14 = StringVar()

check = (root.register(is_valid), '%P')

label_all()
ent_all()

show = partial(show,lb6,number1,number2,number3,number4,number9,number10,number11)
show1 = partial(show1,lb26,number5,number6,number7,number8)

btn1 = Button(text='Вычислить', font='Arial 11 bold',bg='grey',
              bd=5,width=15,height=1,command=show)
btn1.place(x=6,y=250)

btn2 = Button(text='Вычислить', font='Arial 11 bold',bg='grey',
              bd=5,width=15,height=1,command=show1)
btn2.place(x=200,y=250)

btn3 = Button(text='Очистить', font='Arial 11 bold',bg='grey',
              bd=5,width=15,height=1,command=clears)
btn3.place(x=800,y=250)


root.mainloop()