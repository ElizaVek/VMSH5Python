from tkinter import *

def funk1():
    value = c.get() + "1"
    c.delete(0, END)
    c.insert(0, value)
def funk2():
    value = c.get() + "2"
    c.delete(0, END)
    c.insert(0, value)
def funk0():
    value = c.get() + "0"
    c.delete(0, END)
    c.insert(0, value)
    
def funk_plus():
    value = c.get() + "+"
    c.delete(0, END)
    c.insert(0, value)
def funk_minus():
    value = c.get() + "-"
    c.delete(0, END)
    c.insert(0, value)

def funk_ravn():
    value = c.get()
    c.delete(0, END)
    c.insert(0, eval(value))


w = Tk()
w.geometry("240x310")
w.config(bg="#ACF2EB")
w.title("Calculator")

c = Entry(w, justify=RIGHT)
c.grid(row=0, column=0, columnspan=4, sticky="we", padx=5, pady=10)

b1 = Button(w, text='0', bd=5, command=funk0, bg="#DAFD2C")
b1.grid(row=1, column=0, sticky="wens", padx=5, pady=5)
b2 = Button(w, text='1', bd=5, command=funk1, bg="#DAFD2C")
b2.grid(row=1, column=1, sticky="wens", padx=5, pady=5)
b3 = Button(w, text='2', bd=5, command=funk2, bg="#DAFD2C")
b3.grid(row=1, column=2, sticky="wens", padx=5, pady=5)

b_plus = Button(w, text='+', bd=5, command=funk_plus, bg="#1AF321")
b_plus.grid(row=1, column=3, sticky="wens", padx=5, pady=5)
b_minus = Button(w, text='-', bd=5, command=funk_minus, bg="#1AF321")
b_minus.grid(row=2, column=3, sticky="wens", padx=5, pady=5)
b_ravn = Button(w, text='=', bd=5, command=funk_ravn, bg="#FFA200")
b_ravn.grid(row=2, column=0, columnspan=3, sticky="wens", padx=5, pady=5)

w.grid_columnconfigure(0, minsize=60)
w.grid_columnconfigure(1, minsize=60)
w.grid_columnconfigure(2, minsize=60)
w.grid_columnconfigure(3, minsize=60)
w.grid_rowconfigure(0, minsize=60)
w.grid_rowconfigure(1, minsize=60)
w.grid_rowconfigure(2, minsize=60)
w.grid_rowconfigure(3, minsize=60)
w.grid_rowconfigure(4, minsize=60)

w.mainloop()