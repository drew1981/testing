from tkinter import *

root = Tk()

def myClick():                          #questa funzione crea un label dentro la finestra quando si preme il punsante
    myLabel = Label(root, text="On") 
    myLabel.pack()

il_mio_pulsante = Button(root, text="Click!", padx=50, pady=40, activebackground="Green", command=myClick)
il_mio_pulsante.pack()


root.mainloop()