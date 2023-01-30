from tkinter import *
 
def Rb_func():
    if Rb_Var.get() == 4:   
        print("ВСЁ ПРАВИЛЬНО!")
    else:
        print("ПРАВИЛЬНЫЙ ОТВЕТ 5")
    
        
window = Tk()
window.geometry("800x500")
window.config(bg="#CD5E5E")
window.title("Tkinter is new")

Lab = Label(window, text='РЕШИТЕ УРАВНЕНИЕ 5X + 17 = 41', bg="Orange") 
Lab.pack()
Rb_Var = IntVar()   
Rb1 = Radiobutton(text  = "3", variable=Rb_Var, value = 1)
Rb2 = Radiobutton(text  = "17", variable=Rb_Var, value = 2)
Rb3 = Radiobutton(text  = "2", variable=Rb_Var, value = 3)
Rb4 = Radiobutton(text  = "5", variable=Rb_Var, value = 4)
butt1 = Button(text = 'проверка', command = Rb_func)
Rb1.pack()
Rb2.pack()
Rb3.pack()
Rb4.pack()
butt1.pack()
window.mainloop()

    