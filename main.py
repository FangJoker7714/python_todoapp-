# -*- coding: utf8 -*-
from tkinter import messagebox as tkMessageBox
import sys
import tkinter

#画面表示
root = tkinter.Tk()
root.title("todo list")
root.geometry("400x400")

def check(event):
    global Val1
    global Val2
    global Val3
    global Val4
    global Val5
    global Val6
    global Val7

    text=""

    if Val1.get() == True:
        text += ""
    else:
        text += "You forget checking 1."

    if Val1.get() == True:
        text += ""
    else:
        text += "You forget checking 2."

    if Val1.get() == True:
        text += ""
    else:
        text += "You forget checking 3."

    if Val1.get() == True:
        text += ""
    else:
        text += "You forget checking 4."

    if Val1.get() == True:
        text += ""
    else:
        text += "You forget checking 5."

    if Val1.get() == True:
        text += ""
    else:
        text += "You forget checking 6."

    if Val1.get() == True:
        text += ""
    else:
        text += "You forget checking 7."

    tkMessageBox.showinfo('info',text)

#タイトル
back = tkinter.PhotoImage(file="back.png")
canvas = tkinter.Canvas(bg="black", width=400, height=400)
canvas.place(x=0, y=0)
canvas.create_image(0, 0, image=back, anchor=tkinter.NW)

static = tkinter.Label(root,text="Lets programming your life")
static.place(x=120, y=10)


#チェックボックス群
Val1 = tkinter.BooleanVar()
Val2 = tkinter.BooleanVar()
Val3 = tkinter.BooleanVar()
Val4 = tkinter.BooleanVar()
Val5 = tkinter.BooleanVar()
Val6 = tkinter.BooleanVar()
Val7 = tkinter.BooleanVar()

CheckBox1 = tkinter.Checkbutton()
CheckBox1.place(x=0, y=50)

CheckBox2 = tkinter.Checkbutton()
CheckBox2.place(x=0, y=90)

CheckBox3 = tkinter.Checkbutton()
CheckBox3.place(x=0, y=130)

CheckBox4 = tkinter.Checkbutton()
CheckBox4.place(x=0, y=170)

CheckBox5 = tkinter.Checkbutton()
CheckBox5.place(x=0, y=210)

CheckBox6 = tkinter.Checkbutton()
CheckBox6.place(x=0, y=250)

CheckBox7 = tkinter.Checkbutton()
CheckBox7.place(x=0, y=290)

button1 = tkinter.Button(root, text=u'check',width=30)
button1.bind("<Button-1>",check)
button1.place(x=180, y=350)

#項目入力欄群
EditBox1 = tkinter.Entry(width=50)
EditBox1.insert(tkinter.END,"")
EditBox1.place(x=50, y=50)

EditBox2 = tkinter.Entry(width=50)
EditBox2.insert(tkinter.END,"")
EditBox2.place(x=50, y=90)

EditBox3 = tkinter.Entry(width=50)
EditBox3.insert(tkinter.END,"")
EditBox3.place(x=50, y=130)

EditBox4 = tkinter.Entry(width=50)
EditBox4.insert(tkinter.END,"")
EditBox4.place(x=50, y=170)

EditBox5 = tkinter.Entry(width=50)
EditBox5.insert(tkinter.END,"")
EditBox5.place(x=50, y=210)

EditBox6 = tkinter.Entry(width=50)
EditBox6.insert(tkinter.END,"")
EditBox6.place(x=50, y=250)

EditBox7 = tkinter.Entry(width=50)
EditBox7.insert(tkinter.END,"")
EditBox7.place(x=50, y=290)
root.mainloop()
