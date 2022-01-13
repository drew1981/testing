from tkinter import *

root = Tk()

campo_inserimento = Entry(root, width=50, bg="yellow") #creo il campo inserimento
campo_inserimento.pack()
campo_inserimento.insert(0, "Scrivi Il Tuo Nome")


def myClick():
    
    myLabel = Label(root, text=campo_inserimento.get()) # <<-----------viene creato un label con scritto con il valore del campo_inserimento---
    myLabel.pack() #                                                                                                                          |
#                                                                                                                                             |
il_mio_pulsante = Button(root, text="Click!", padx=50, pady=40, activebackground="Green", command=myClick) #creo un pulsante                  |
il_mio_pulsante.pack()                                                                                     # che quando viene premuto         |
                                                                                                            # richiama la funzione myClick----


root.mainloop()