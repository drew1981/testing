from tkinter import *

#creo una ----------FINESTRA--------------

f = Tk()                        #istanzio una finestra

f.title("Programma Drew")       #titolo finestra
f.geometry("800x600")           #dimensionare la finestra
f.configure(background="grey")

#posso creare quante finestre voglio:

f1 = Tk()                        #istanzio una finestra

f1.title("Drew")                 #titolo finestra
f1.geometry("400x300")           #dimensionare la finestra
f1.configure(background="yellow")

def Check_Button():
    print("La casella è ok")

#definiamo una funzione richiamabile dal pulsante va dichiarata PRIMA del pulsante

def pulsante1_premuto(): #  <-----------------------------------------------|
    print("pulsante1 ok")  # stampa sulla shell                             |    
#                                                                           |
def pulsante_premuto():  #  <--------------------------------               |
    print("pulsante ok")   # stampa sulla shell             |               |
#                                                           |               |
#creo un -----------PULSANTE--------------                  |               |
#                                                           |               |
b = Button(f, text="Premi Qui", command=pulsante_premuto) #--               |
b.pack() #-----------ogni widgets creato va packizzato in questo modo       |
#                     ma si può usare anche .grid(coloumn=0, row=0)         |
#creo altro pulsante                                                        |
#                                                                           !
b1 = Button(f, text="Submit", command=pulsante1_premuto) #definisco comando--
b1.pack(pady=10)

#creo un --------CHECK BUTTON---------

casella = Checkbutton(f, text="Seleziona Qui", command=Check_Button)
casella.pack(pady=10)


#creo una----------CASELLA DI TESTO------------

casella_testo = Entry(f) # si usa Entry e si associa alla finestra (f)
casella_testo.pack(pady=10) #qui definisco la posizione sull'asse Y


#testo  =  Label(f, text="Drew") #per aggiungere un'etichetta all'interno dell'interfaccia
#testo.pack(side=BOTTOM)



f.mainloop()
