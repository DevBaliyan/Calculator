from tkinter import *
#import tkinter

def btn(numbers):
    global operator
    operator += str(numbers)
    text_Input.set(operator)

def eq():
    global operator
    s = str(eval(operator))
    text_Input.set(s)
    operator = s  


def clr():
    global operator
    operator = ''
    text_Input.set('')


tk = Tk()
tk.title('CALCULATOR')
tk.geometry('315x550')
text_Input = StringVar()
operator = ''
frame = Entry(tk, relief=RAISED, borderwidth=5, cursor='circle', highlightcolor='green', justify=RIGHT
              , font=('italic', 25), bg='powder blue', highlightthickness=8, textvariable=text_Input)
frame.pack(side=LEFT, fill=X)
frame.place(bordermode=OUTSIDE, height=85, width=308, x=5, y=0)

frame1 = Frame(tk, relief=RAISED, borderwidth=5, cursor='arrow', highlightcolor='green',
               bg='powder blue', highlightthickness=8)

frame1.pack(side=BOTTOM, fill=X)
frame1.place(bordermode=OUTSIDE, height=452, width=308, x=5, y=80)

b1 = Button(frame1, text='1', command=lambda: btn(1), height=4, width=12, bg='#78F',
            relief=RIDGE, activebackground='#45F')
b1.grid(row=0, column=0)

b2 = Button(frame1, text='2', command=lambda: btn(2), height=4, width=12, bg='#78F',
            relief=RAISED, activebackground='#45F', cursor='heart')
b2.grid(row=0, column=1)

b3 = Button(frame1, text='3', command=lambda: btn(3), height=4, width=12, bg='#78F',
            relief=RIDGE, activebackground='#45F', cursor='fleur')
b3.grid(row=0, column=2)

b4 = Button(frame1, text='4', height=4, width=12, bg='#78F', command=lambda: btn(4),
            activebackground='#45F', cursor='plus')
b4.grid(row=1, column=0)

b5 = Button(frame1, text='5', height=4, width=12, bg='#78F', command=lambda: btn(5),
            relief=RIDGE, activebackground='#45F', cursor='spraycan')
b5.grid(row=1, column=1)

b6 = Button(frame1, text='6', height=4, width=12, bg='#78F', command=lambda: btn(6),
            activebackground='#45F', cursor='star')
b6.grid(row=1, column=2)

b7 = Button(frame1, text='7', height=4, width=12, bg='#78F', command=lambda: btn(7),
            relief=RIDGE, activebackground='#45F', cursor='tcross')
b7.grid(row=2, column=0)

b8 = Button(frame1, text='8', height=4, width=12, bg='#78F', command=lambda: btn(8),
            activebackground='#45F', cursor='shuttle')
b8.grid(row=2, column=1)

b9 = Button(frame1, text='9', height=4, width=12, bg='#78F', command=lambda: btn(9),
            relief=RIDGE, activebackground='#45F', cursor='sizing')
b9.grid(row=2, column=2)

b10 = Button(frame1, text='.', height=4, width=12, cursor='trek', command=lambda: btn('.'),)
b10.grid(row=3, column=0)

b11 = Button(frame1, text='0', height=4, width=12, bg='#3F5',  command=lambda: btn(0),
             relief=RIDGE,  cursor='arrow')
b11.grid(row=3, column=1)

b12 = Button(frame1, text='/', height=4, width=12, background='#3F8', command=lambda: btn("/"),
             activebackground='#45F', cursor='dotbox')
b12.grid(row=3, column=2)

b13 = Button(frame1, text='+', height=4, width=12, background='#3F8',  command=lambda: btn("+"),
             relief=RIDGE, activebackground='#45F', cursor='man')
b13.grid(row=4, column=0)

b14 = Button(frame1, text='-', height=4, width=12, background='#3F8',  command=lambda: btn("-"),
             activebackground='#45F', cursor='plus')
b14.grid(row=4, column=1)

b15 = Button(frame1, text='x', height=4, width=12,  command=lambda: btn("*"),
             background='#3F8', activebackground='#0033FF', cursor='cross')
b15.grid(row=4, column=2)

eq = Button(frame1, text='=', height=4, width=22,  command=eq,
            background='#3F8', activebackground='#0033FF', cursor='cross')
eq.grid()
eq.place(x=2, y=356)

cl = Button(frame1, text='C', height=4, width=15,  command=clr,
            background='#3F8', activebackground='#0033FF', cursor='cross')
cl.grid()
cl.place(x=167, y=356)

tk.mainloop()
