from tkinter import *

root = Tk()
root.title("++--C4LC0L47R1C3--++")
root.configure(background="grey")

campo_inserimento = Entry(root, width=28, font=('Georgia 10'), bg="Orange", borderwidth=8)
campo_inserimento.grid(row=0, column=0, columnspan=4, padx=20, pady=20, ipady=20)
#campo_inserimento.configure(font="KaiTi 12")

def button_click(numero):
    campo_inserimento.insert(END, numero)
    
def button_clear():
    campo_inserimento.delete(0, END)
    
def button_add():
    primonumero = campo_inserimento.get()
    global f_num
    f_num = int(primonumero)
    campo_inserimento.delete(0, END)
    
def button_equal():
    secondonumero = campo_inserimento.get()
    campo_inserimento.delete(0, END)
    campo_inserimento.insert(0, f_num + int(secondonumero))
    
# definisco i tasti

tasto1 = Button(root, text="1", bg="grey", padx=45, pady=30, command=lambda: button_click(1))
tasto2 = Button(root, text="2", bg="grey", padx=45, pady=30, command=lambda: button_click(2))
tasto3 = Button(root, text="3", bg="grey", padx=45, pady=30, command=lambda: button_click(3))
tasto4 = Button(root, text="4", bg="grey", padx=45, pady=30, command=lambda: button_click(4))
tasto5 = Button(root, text="5", bg="grey", padx=45, pady=30, command=lambda: button_click(5))
tasto6 = Button(root, text="6", bg="grey", padx=45, pady=30, command=lambda: button_click(6))
tasto7 = Button(root, text="7", bg="grey", padx=45, pady=30, command=lambda: button_click(7))
tasto8 = Button(root, text="8", bg="grey", padx=45, pady=30, command=lambda: button_click(8))
tasto9 = Button(root, text="9", bg="grey", padx=45, pady=30, command=lambda: button_click(9))
tasto0 = Button(root, text="0", bg="grey", padx=45, pady=30, command=lambda: button_click(0))

button_add = Button(root, text="+", bg="grey", padx=45, pady=20, relief="raised", activebackground="orange", highlightbackground="orange", command=button_add)
button_equal = Button(root, text="=", bg="grey", padx=45, pady=20, relief="raised", activebackground="green", highlightbackground="green", command=button_equal)
button_clear = Button(root, text="Clr", bg="grey", padx=40, pady=20, command=button_clear)

#metto i tasti a schermo

tasto1.grid(row=3, column=0)
tasto2.grid(row=3, column=1)
tasto3.grid(row=3, column=2)

tasto4.grid(row=2, column=0)
tasto5.grid(row=2, column=1)
tasto6.grid(row=2, column=2)

tasto7.grid(row=1, column=0)
tasto8.grid(row=1, column=1)
tasto9.grid(row=1, column=2)

tasto0.grid(row=4, column=1)

button_add.grid(row=5, column=1)
button_equal.grid(row=5, column=2)
button_clear.grid(row=5, column=0)

root.eval('tk::PlaceWindow . center')
root.mainloop()