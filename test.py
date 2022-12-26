#https://www.tutorialkart.com/python/tkinter/button/
#$ git push --set-upstream origin Future_1  добавить ветку на github

from tkinter import *
from datetime import datetime as dt
root = Tk()
root["bg"] = "#159"
root.geometry("600x600+0+0")
root.title("test")
#root.resizable(0,0)

def test():
    print("test")
    btn2.config(state=['disabled'])

def labchange():

    lbl1.config(fg="red",bg="#456") 
    lbl1["text"] = ent1.get()  

def zoomtext(event):
    lbl1.config(font='Arial 15 bold')

def vremy(event):
    ent1.delete(0,END)
    t = dt.now().time()
    ent1.insert(0,t.strftime("%H:%M:%S  "))   

def rad0():
    root["bg"] = "#159"   

def rad1():
    root["bg"] = "#789" 

def rad2():
    root["bg"] = "#666" 

def rad3():
    root["bg"] = "#247"   

def rad4():
    root["bg"] = "#357" 

def rad5():
    root["bg"] = "#555"   
    

btn1 = Button(root, # форма расположение
            text="test",  # текст 
            font="Arial 10 bold", #шрифт
            fg="blue", # цвет текста
            bd=5, # отступы границы кнопки
            bg="gray", # цвет кнопки в не нажатом положении
            width=0, # ширина кнопки
            height=0, # высота кнопки
            padx=0, # ширина кнопки
            pady=0, # высота кнопки
            activebackground='gray', # цвет кнопки в нажатом положении
            activeforeground="white", # цвет текста в нажатом положении
            highlightbackground="green", # цвет рамки выделения когда виджит теряет фокус 
            command=test # команда вызывает функцию
            ) #state=['disabled'],  state=['active'], # статус кнопки актиности
btn1.place(x=0, y=50) #anchor="c" 

btn2 = Button(root,text="   Disable   ", width=20, command=labchange)
btn2.grid(row=0, column=0)

python_logo = PhotoImage(file="./sdefgfhg.png")
lbl2 = Label(root, image=python_logo)
lbl2.grid(row=1, column=2) 

lbl1 = Label(root,text="testlabel",fg='white', bg='#145', font='Arial 10 bold',width=10,height=2)
lbl1.grid(row=1, column=1)

lbl1.bind("<Motion>", zoomtext)

ent1 = Entry(width=50)
ent1.grid(row=0,column=2)

ent1.bind("<Button-1>", vremy)
  

fr1 = Frame(root,width=200,height=200)
fr1.grid(row=2,column=0)

fr2 = Frame(root,width=200,height=200)
fr2.grid(row=2,column=1)


var1 = IntVar()
var1.set(0)
radio0 = Radiobutton(fr1,text="Radiobutton0",variable=var1,value=0,bg="#159",fg="green",command=rad0)
radio1 = Radiobutton(fr1,text="Radiobutton1",variable=var1,value=1,bg="#789",fg="blue",command=rad1)
radio2 = Radiobutton(fr1,text="Radiobutton2",variable=var1,value=2,bg="#666",fg="red",command=rad2)

radio0.grid(row=0,column=0)
radio1.grid(row=1,column=0)
radio2.grid(row=2,column=0)

var2 = IntVar()
var2.set(0)
radio3 = Radiobutton(fr2,text="Radiobutton3",variable=var2,value=0,bg="#247",fg="green",command=rad3)
radio4 = Radiobutton(fr2,text="Radiobutton4",variable=var2,value=1,bg="#357",fg="blue",command=rad4)
radio5 = Radiobutton(fr2,text="Radiobutton5",variable=var2,value=2,bg="#555",fg="red",command=rad5)

radio3.grid(row=0,column=0)
radio4.grid(row=1,column=0)
radio5.grid(row=2,column=0)


root.mainloop()
