from tkinter import *

def scrivi(evento):
    print(lista.curselection())

def esci():
    f.destroy()
    
f = Tk()                      

f.title("Programma Drew")      
f.geometry("800x600")           
f.configure(background="grey")

lista = Listbox(f)
lista.pack()
lista.insert(END, "Uno", "Due", "Tre") #in questo modo inseriamo gli elementi dopo l'ultimo elemento
#######lista.insert(0, "Inizio")               # se volessi inserire valori tramite indice
lista.bind("<ButtonRelease-1>", scrivi) #imposta un'azione alla pressione del tasto sinistro del mouse e lo associa ad una funzione (scrivi)

b1 = Button(f, text="Esci", command=esci)
b1.pack()


f.mainloop()