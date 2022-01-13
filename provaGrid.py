from tkinter import *

root = Tk()

#creo un Label Widget

myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="Hello Drew")


#li rendo visibile all'interno della finestra root e imposto la posizione con .grid

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)












root.mainloop()
