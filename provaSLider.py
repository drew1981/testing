from tkinter import *

def esegui():
    print(slider.get())
    
def esci():
    f.destroy()

f = Tk()                      

f.title("Programma Drew")      
f.geometry("200x200")           
f.configure(background="grey")


slider = Scale(f, from_=0, to_=9, orient=HORIZONTAL, activebackground="yellow")
slider.pack(pady=10)

b = Button(f, text="Submit", activebackground="yellow", command=esegui)
b.pack(pady=10)

b1 = Button(f, text="Esci", command=esci)
b1.pack()

f.mainloop()