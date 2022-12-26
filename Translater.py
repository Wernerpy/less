#program for translating from Russian into English

from cgitb import text
from email import header
from fnmatch import translate
from gettext import translation
from tkinter import *
from tkinter import ttk
from googletrans import Translator


#text translation function
def translate():
    for language, suffix in languages.items():
        if comboTwo.get() == language:
            text = t_input.get('1.0', END)
            translation = translator.translate(text, dest=suffix)
            t_output.delete('1.0', END)
            t_output.insert('1.0',translation.text)


#creating the main window
root = Tk()
root.geometry('500x340+0+0')
root.title('Переводчик')
root.resizable(0,0)
root['bg'] = '#555'

#class
translator = Translator()

#dictionary with languages
languages = {'Русский': 'ru', 'Английский': 'en', 'Французский': 'fr'}

#top Frame
header_frame = Frame(root, bg='#783')

#stretch in length
header_frame.pack(fill=X)

#central arrow Frame
header_frame.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(1, weight=1)
header_frame.grid_columnconfigure(2, weight=1)

#first left Combobox
comboOne = ttk.Combobox(header_frame,values=[lang for lang in languages], state='readonly')
comboOne.current(0)
comboOne.grid(row=0, column=0, pady=0, padx=0)

#Label with an arrow at the top
label = Label(header_frame, fg='black', bg='#783', font='Arial 20 bold',text='=>')
label.grid(row=0, column=1,pady=2)

#Text from the left Text input
lab=Label(root, text='Text input\nВвод текста', font='Arial 10 bold',bg='#783')
lab.place(x=0,y=50)

#Text from the left Output text
lab1=Label(root, text='Text Output\nВывод текста', font='Arial 9 bold',bg='#783')
lab1.place(x=0,y=160)

#second right Combobox
comboTwo = ttk.Combobox(header_frame, values=[lang for lang in languages], state='raedonly')
#Текущий/current/the language is automatically set to combo box
comboTwo.current(1)
comboTwo.grid(row=0,column=2)

#first text entry window
t_input = Text(root, width=40, height=5, font='Arial 12 bold',bg='#999')
t_input.place(x=90, y=50)

#text translation button
btn = Button(root, width=40, height=2, text='__________Перевести => Translate__________', font='Arial 15 bold',bg='#783', command=translate)
btn.place(x=5,y=270)

#second window for displaying the translated text
t_output = Text(root, width=40, height=5, font='Arial 12 bold',bg='#999')
t_output.place(x=90, y=160)

#program cycle
root.mainloop()



