from tkinter import *

def esci():
    f.destroy()

f = Tk()                      

f.title("EDITOR Drew")      
f.geometry("800x600")           
f.configure(background="grey")

editor = Text(f, font="Thaoma")
editor.pack()

b = Button(f, text="Esci", command=esci)
b.pack()


f.eval('tk::PlaceWindow . center')
f.mainloop()