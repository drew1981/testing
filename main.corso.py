#Primo Programma


messaggio = input("Inserisci un dato ")
print(messaggio)
if 1 < 5:
    print("Hai vinto " + messaggio)
print("Game Over")


#VARIABILI
#è come una scatola che contiene un valore
#il valore può cambiare ma la "scatola" non cambia

x = 5
y = 6

città = "Roma", "Reggio"

print(x,y,città)

#possono essere chiamate in qualsiasi modo ma
#evitando spazi e trattini

#valori multipli

x, y, z = 100, 567, 789
k = x + y + z
print(k)
print(x,y,z)
print(x)
print(y)
print(z)





##################################--------------------Tipi di dati-----------------------#######################################



# str   x = "Ciao"
# int   x = 20
# float x = 20.5
# bool  x = True oppure False




################################----------------------COLLEZIONI DI DATI----------------######################################



# list  x = ["Roma", "Milano", "Reggio"]
# tuple x = ("Roma", "Milano", "Reggio")
# range x = range(6)
# dict  x = {"nome": "Andrea", "età": 41}
# set   x = {"Roma", "Milano", "Reggio"}




#per capire che tipo di variabile stiamo utilizzando:
x = ("Roma", "Milano", "Reggio")
print(type(x))

#Casting
# prendere il valore di una variabile, 
# tipo str e convertirlo in int ad esempio.

#       x = 5
#       y = "5"

#       print(x + y)

#in questo modo otteniamo un errore in quanto sommerebbe
#un int con un str
#deve essere scritto:

x = 5
y = int("5")

print(x * y) 

#oppure trasformare un int in float

x = float(5)
print(x)

# Lavorare con le stringhe
# se vogliamo scrivere una stringa multi riga si usano tre doppi apici """prova"""

x = """Ciao
sto facendo 
una prova 
multilinea"""
y = """Se vedi
questo messaggio
sta funzionando"""

print(x, y)

#trattare le stringhe come array
#le stringhe sono viste come un insieme di caratteri ordinati da 0 a infinito
#vediamo un esempio:

x = """Ciao
sto facendo 
una prova 
multilinea"""

print(x[11])

#in questo caso il print restituisce c che sarebbe l'undicesimo carattere della stringa

x = "prova"
y = "foo"

print(x[3])                 #stampa v (si inizia sempre da zero)

#possiamo anche contare i caratteri di una stringa

x = "il fine giustifica il mezzo"

print(len(x))

#possiamo prendere anche solo una parte di una stringa

x = "il fine giustifica il mezzo"

print(x[3:12])              #da 3 a 12 il risultato fine giusti (si parte da 0)
print(x[:12])              #se volessimo prendere dall'inizio basterebbe omettere il primo numero il fine gius

#possiamo usare le funzioni upper e lower per TUTTO MAIUSCOLO o tutto minuscolo

x = "il fine giustifica il mezzo"

print(x.upper())            #IL FINE GIUSTIFICA IL MEZZO

x = "IL FINE GIUSTIFICA IL MEZZO"

print(x.lower())            #il fine giustifica il mezzo

#possiamo utilizzare la funzione replace

x = "il fine giustifica il mezzo"

print(x.replace("i", "o"))  #ol fone goustofoca ol mezzo

#possiamo concatenare

x = "prova"
y = "foo"

print(x + y)

##############################-----format-------- è una funzione molto interessante per inserire dei valori all'interno di una stringa

x = 41

variabile1 = "Mi chiamo Andrea e ho {} anni"

print(variabile1.format(x))

x = 41
y = 80
z = 1.70

variabile1 = "Mi chiamo Andrea e ho {} anni peso {} e sono alto {} metri"

print(variabile1.format(x, y, z))

#possiamo utilizzare anche i valori, in ordine, dichiarati nella print quindi:

variabile1 = "Mi chiamo Andrea e ho {} anni peso {} e sono alto {} metri"

print(variabile1.format(41, 80, 1.70))

#possiamo utilizzare anche gli indici quindi:

variabile1 = "Mi chiamo Andrea e ho {0} anni peso {1} e sono alto {2} metri"

print(variabile1.format(41, 80, 1.70))
                        #0  #1   #2
                        
# possiamo fare un escape dei caratteri con backslash \






######################################---------I VALORI BOOLEANI ovvero True e False-----------####################################


x = True
y = False

print(5 < 10) 
print(11 > 3)        
# possiamo inserire tutto il un if-else e quindi:

if 5 < 10:                  #se il valore < di 10 scrive va bene
    print("va bene")
else:
    print("non va bene")    #se il valore > di 10 scrive non va bene
    
    

# possiamo valutare i valori delle variabili

print(bool(1)) #true
print(bool(0)) #false

# i valori sempre False sono:

# bool(False)
# bool(None)
# bool(0)
# bool("")
# bool(())
# bool([])
# bool({})

pane = 0

if pane:
    print("non serve comprarlo")
else:
    print("comprare pane")
    
#altro esempio con lista

lista_della_spesa = []      #la lista è vuota quindi la print sarà: non andare al supermercato

if lista_della_spesa:
    print("andrea al supermercato")
else:
    print("non andare al supermercato")
    

    
lista_della_spesa = ["Birra", "Pane", "Vino"]      #la lista non è vuota quindi la print sarà: andare al supermercato

if lista_della_spesa:
    print("andare al supermercato")
else:
    print("non andare al supermercato")
    
#operazioni aritmetiche + - * / %(modulo, resto della divisione) ** (potenza)

x = 3
y = 7

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x ** y)  
print(x % y)

print((x + 3456) * 2 / y)

#ora vediamo un esempio in cui aggiungiamo alla variabile x un valore dichiarato successivamente sempre sulla stessa variabile

x = 23
x += 56    

print(x)

#possiamo utilizzare questo metodo con tutti gli operatori (+=, *= ecc.)
    
x = 23
x *= 56    

print(x)   

# FUNZIONI min max abs e pow

x = min(234, 5876595, 4874, 57)    #minimo tra numeri

print(x)

x = max(234, 5876595, 4874, 57)    #massimo tra numeri

print(x)

x = abs(-234)                      #valore assoluto

print(x)

x = pow(57,2)                      #potenza di un numero

print(x)

#se volessimo fare operazioni più complesse dovremmo importare il modulo MATH




#################################################--------IF-----------############################################################

x = 10
if x < 11:                           # < minore
    print("condizione verificata")
    print("è un numero intero")
    print("va bene")
print("non sono nell'IF")            #tutto quello che non è identato non fa parte dell'if!!!

x = 11
if x == 11:                          # == corrisponde a uguale a si distingue dall' = che serve per dichiarare un valore di una var
    print("condizione verificata")
    print("è un numero intero")
    print("va bene")

x = 10
if x != 11:                          # != diverso
    print("condizione verificata")
    print("è un numero intero")
    print("va bene")
    
    
# si possono utilizzare sintassi tipo x compreso tra:
x = 11
if 5 <= x <= 89:
    print("x è compreso tra 5 e 89")
else:
    print("x non è compreso tra 5 e 89")
    
    
# si possono utilizzare ovviamente maggiore > minore uguale <= maggiore uguale >= ECC ECC




####################################################--------ELSE----------##############################################

x = 10
if x != 11:                          # != diverso
    print("condizione verificata")
    print("è un numero intero")
    print("va bene")
else:
    print("condizione non verificata")
    
x = 11
if x == 11:                          # == corrisponde a uguale a si distingue dall' = che serve per dichiarare un valore di una var
    print("condizione verificata")
    print("è un numero intero")
    print("va bene")
else:
    print("condizione non verificata")
    
##############################--------ELIF--------- serve ad impostare più condizioni#########################################

x = 11
if x == 11:                          
    print("condizione verificata")
elif x > 10:
    print("x è maggiore di 10")
else:
    print("x è minore di 10")

###########################################--------OPERATORI LOGICI AND e OR--------#########################################################

# AND si devono verificare tutte le condizioni

x = 11
if x > 10 and x < 20:
    print("x compreso tra 10 e 20")
else:
    print("x non è compreso tra 10 e 20")

x = 5
y = 8
if x < 10 and y > 2:
    print("condizione verificata")    ######questo è il risultato
else:
    print("condizione non verificata")
    
# OR si deve verificare almeno una delle condizioni

x = 5
y = 8
if x < 10 or y > 2:
    print("condizione verificata")     ######questo è il risultato
else:
    print("condizione non verificata")
    

x = 5
y = 8
if x == 10 or y == 2:
    print("condizione verificata")
else:
    print("condizione non verificata") ######questo è il risultato
    
# NOT serve per negare la condizione

x = 5
if not(x < 10):
    print("x non è minore di 10")
else:
    print("x è minore di 10")    ######questo è il risultato
    
x = 11
if not(x < 10):
    print("x non è minore di 10")  ######questo è il risultato
else:
    print("x è minore di 10")

# ---------versione shot hand di IF----------

x = 8
print("x è <=10") if x <= 10 else print("x non è <=10")

# IF annidiati

x = 4
if x % 2 == 0:                              #utilizzo il resto della divisione % che deve essere uguale a 0 
                                            #quindi i numeri pari danno resto 0 quelli
                                            #dispari danno un numero diverso da 0
    if(x < 10):
        print("numero pari e minore di 10")
    if(x == 4):
        print("x è 4!")
else:
    print("numero dispari...")

##############################################--------CICLO WHILE-------############################################################


i = 0           #dobbiamo impostare una variabile, in questo caso i che chiamiamo CONTATORE
while i < 6:    #utilizziamo la funzione while per dire ad esempio "mentre i è minore di 6" scrivi i a schermo, 
                #poi aggiungi 1 ad i fino a quando i sarà uguale a 6 e quindi non più minore di 6, al quel punto scrivi OK
    print(i)
    i += 1      #aumento i di 1
print("OK")

# ---------l'output di questo codice è:----------
# 0
# 1
# 2
# 3
# 4
# 5
# OK

###################################-------BREAK----------per interrompere il ciclo while#############################################

i = 0           
while i < 6: 
    print(i)
    if i == 3:
        break    #quando i sarà uguale a 3 interrompe il ciclo while e va sul print OK
    i += 1
print("OK")

#---------CONTINUE----------salta una iterazione che assegnamo

#i = 0           
#while i < 6: 
#    print(i)
#    if i == 3:
#        continue    #quando i sarà uguale a 3 il ciclo while ricomincia e poi va avanti (quando i = 4)
#    i += 1
#print("OK")

##########################################-----------------CICLO FOR----------------------############################################
#serve ad iterare una lista una stringa o un range

lista_elementi = ["Elemento1", "Elemento2", "Elemento3"]
stringa = "Anguria"

for carattere in stringa:
    print(carattere)

for elemento in lista_elementi:
    print(elemento)

for x in range(9):
    print(x)
    
#si possono usare anche tanti for:

for riga in range(4):
    for colonna in range(4):
        print("(" + str(riga) + ":" + str(colonna) + ")")

#possiamo usare, come per il WHILE le istruzioni ELSE, BREACK, CONTINUE...e possiamo annidiare gli IF




#################################-----------COLLEZIONI DI DATI----------------########################################################

# LISTE         sono collezioni ordinate e modificabili. Permettono duplicati
# TUPLE         sono collezioni ordinate non modificabili. Permettono duplicati
# DICTIONARY    sono collezioni ordinate e modificabili. Non permettono duplicati
# SET           sono collezioni non ordinate, non indicizzate. Non permettono duplicati



# #######################################-----------LISTE----------()
# len()   type()    list()

x = ["Milano", "Roma", "Milano"] #le parentesi quadre identificano una lista

#possiamo utilizzare anche il costruttore list quindi lo stesso risultato si ottine con:
x = list(("Milano", "Roma", "Milano"))
          
y = ["Ciao", 808, False]


print(type(x))     #vedere tipo lista
print(len(y))      #vedre lunghezza lista

#invocare elementi di una lista con indice

y = ["Ciao", 808, False]

print(y[1]) # output 808

#invocare elementi di una lista con range

y = ["Ciao", 808, False, "Andrea", 1981, True, 12.90, "Va bene"]

print(y[1:4]) # da 1 a 4, output: [808, False, 'Andrea']

print(y[2:]) # da 2 alla fine della lista

print(y[-4]) # invocare elementi a ritroso inserendo -

#-----verificare se esiste elemento in una lista------

y = ["Ciao", 808, False, "Andrea", 1981, True, 12.90, "Va bene"]

if "Andrea" in y:
    print("si esiste")

# --------modificare la lista tramite invocazione indice e riassegnare valore-----

y = ["Ciao", 808, False, "Andrea", 1981, True, 12.90, "Va bene"]
y[4] = 41
print(y) # output sarà ['Ciao', 808, False, 'Andrea', 41, True, 12.9, 'Va bene']
                                                    # ^^^
                                                    
# --------modificare la lista tramite invocazione range

y = ["Ciao", "Andrea", "Va bene"]
y[1:3] = ["We", "Di Lallo"]

# --------inserire con APPEND che inserisce in fondo alla lista un elemento-----

x = ["Milano", "Roma", "Reggio"]
x.append("Bergamo")
print(x)
                                                      
# --------inserire con INSERT--------

x = ["Milano", "Roma", "Reggio"]
x.insert(1, "Bergamo")   # inseriamo all'interno della parentesi l'indice dell'elemento da inserire, cioè dove va posizionato
print(x)

# --------inserire con extend---------

x = ["Milano", "Roma", "Reggio"]
y = ["Napoli", "Torino", "Venezia"]
x.extend(y)
print(x)

# possiamo rimuovere un elemento

x = ["Milano", "Roma", "Reggio"]
x.remove("Milano")
print(x)

#con pop eliminiamo l'ultimo elemento
x = ["Milano", "Roma", "Reggio"]
x.pop()
print(x)

#con del invece eliminiamo uno specifico elemento con l'indice

x = ["Milano", "Roma", "Reggio"]
del x [0]  #toglie "Milano"
print(x)

# con clear puliamo la lista

x = ["Milano", "Roma", "Reggio"]
x.clear()  #pulisce la lista
print(x)

# -----LIST COMPREHENSION--------FARE RIFERIMENTO ALLA DOCUMENTAZIONE PER APPROFONDIRE
# espressione for elementi in lista if condizione == True

lista_elementi = ["Pane", "Acqua", "Birra", "Carote"]
[print(elementi) for elementi in lista_elementi if elementi != "Birra"]
#stampa tutti gli elementi in lista_elementi diversi da "Birra"

# ORDINARE UNA LISTA

# SORT
lista_elementi = ["Pane", "Acqua", "Birra", "Carote"]
lista_elementi.sort() #di defaul ordina alfabeticamente gli elementi
print(lista_elementi)
# SORT reverse
lista_elementi = ["Pane", "Acqua", "Birra", "Carote"]
lista_elementi.sort(reverse=True) #ordina al contrario alfabeticamente gli elementi
print(lista_elementi)

# COPIARE UNA LISTA

x = ["Pane", "Acqua", "Birra", "Carote"]
y = x.copy()
print(y)




#############################################--------------TUPLE------------[]




# le modalità sono le stesse usate per le liste. Ma non sono modificabili (anche se esistono metodi per farlo)
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# count ci permette di contare quante volte è presente un elemento in una tupla

lista_elementi = ["Pane", "Acqua", "Birra", "Carote"]
x = lista_elementi.count("Pane")
print(x)

# index ci permette di conoscere l'index di un elemento in una tupla

lista_elementi = ["Pane", "Acqua", "Birra", "Carote"]
x = lista_elementi.index("Pane")
print(x)

# per creare una tupla con costruttore

y = tuple(("Reggio", "Bergamo"))

###############################################------------SET-------------{} 

#non sono indicizzati (quando li mandiamo a schermo, l'ordine è sempre casuale)


x = {"Milano", "Roma", "Napoli"}
print(type(x))
print(len(x))

# per fare un set con un costruttore

y = set(("Reggio", "Bergamo"))

# ---------cicliamo----------

x = {"Milano", "Roma", "Napoli"}

for citta in x:
    print(citta)

# ------verifichiamo se esiste elemento nell set--------SECONDO METODO

x = {"Milano", "Roma", "Napoli"}

print("Milano" in x)    #restituisce True o False a seconda se esiste o meno

# aggiungere elementi   add oppure update

x = {"Milano", "Roma", "Napoli"}
x.add("Venezia") #add

x = {"Milano", "Roma", "Napoli"}
y = {"Venezia", "Bergamo"}

x.update(y)  #update
print(x)

# rimuovere elementi REMOVE e DIASCARD

x = {"Milano", "Roma", "Napoli"}
x.remove("Milano") 
print(x)

x = {"Milano", "Roma", "Napoli"}
x.discard("Milano") # in realtà discard non ci restituisce un errore se l'elemento non esiste, SCARTA ELEMENTI MA non li elimina
print(x)

# possiamo usare clear e del come gli altri tipi di dati

# -------UNION------ unisce gli elementi di x e y CREANDO un altro SET e restituisce un solo valore se duplicato

x = {"Milano", "Roma", "Napoli"}
y = {"Venezia", "Bergamo", "Roma"}

z = x.union(y)
print(z)        ### ci sarà solo una volta "Roma"

#possiamo usare anche UPDATE

# ----------INTERSECTION----------vale la teoria degli insiemi

# ---INTERSECTION_UPDATE---lavora facendo un update dei set già esistenti

x = {"Milano", "Roma", "Napoli", "Venezia", "Bergamo"}
y = {"Milano", "Roma", "Napoli", "Reggio", "Bologna"}
x.intersection_update(y)     #intersection_update restituisce solo i valori in comune
print(x)

# ---INTERSECTION---lavora creando un nuovo set da quelli già esistenti

x = {"Milano", "Roma", "Napoli", "Venezia", "Bergamo"}
y = {"Milano", "Roma", "Napoli", "Reggio", "Bologna"}

z = x.intersection(y)   #intersection restituisce solo i valori in comune
print(z)

# ----------SYMMETRIC_DIFFERENCE----------vale la teoria degli insiemi

# ------SYMMETRIC_DIFFERENCE_UPDATE--lavora facendo un update dei set già esistenti

x = {"Milano", "Roma", "Napoli", "Venezia", "Bergamo"}
y = {"Milano", "Roma", "Napoli", "Reggio", "Bologna"}
x.symmetric_difference_update(y) #symmetric_difference_update restituisce tutti i valori NON in comune
print(x)
 
 
 
# ------SYMMETRIC_DIFFERENCE--lavora facendo un nuovo set dai set già esistenti e restituisce tutti i valori NON in comune

x = {"Milano", "Roma", "Napoli", "Venezia", "Bergamo"}
y = {"Milano", "Roma", "Napoli", "Reggio", "Bologna"}

z = x.symmetric_difference(y)
print(z)

########################################-------------DICTIONARY---------------####################################################

#collezioni di dati ordinati modificabili e non permettono duplicati
#---SONO I CORRISPONDENTI OGGETTI IN JAVA----dove definiamo delle proprietà, delle chiavi

persone = {
    "Nome" : "Andrea",      #questa è una coppia CHIAVE-VALORE ("Nome" è la chiave "Andrea" è il valore)
    "Cognome" : "Di Lallo", #questa è una coppia CHIAVE-VALORE 
    "Eta" : 41            #questa è una coppia CHIAVE-VALORE 
}
print(persone)
print(len(persone))
print(type(persone))

print(persone["Nome"])      #possiamo richiamare le chiavi con le parentesi [] (python ci suggerisce già le chiavi che sono state definite nel DICT)
print(persone["Cognome"])   # e ci restituisce il VALORE delle chiavi
print(persone["Eta"])
#-----OPPURE---------
print(persone.get("Nome"))
print(persone.get("Cognome"))
print(persone.get("Eta"))

# se vogliamo le chiavi-----

print(persone.keys())  #il risultato è: dict_keys(['Nome', 'Cognome', 'Eta'])

#assegnado le chiavi ad una variabile....

persone = {
    "Nome" : "Andrea",      
    "Cognome" : "Di Lallo", 
    "Eta" : 41
}

x = persone.keys()
print(x)

#utilizziamo ITEMS per avere direttamente tutte le TUPLE

persone = {
    "Nome" : "Andrea",      
    "Cognome" : "Di Lallo", 
    "Eta" : 41
}

print(persone.items())     #il risultato sarà: dict_items([('Nome', 'Andrea'), ('Cognome', 'Di Lallo'), ('Eta', 41)])

#assegnado gli items ad una variabile

persone = {
    "Nome" : "Andrea",      
    "Cognome" : "Di Lallo", 
    "Eta" : 41
}
x = persone.items()
print(x)

#-----verificare se esiste classe

persone = {
    "Nome" : "Andrea",      
    "Cognome" : "Di Lallo", 
    "Eta" : 41
}
print("Nome" in persone)  #True

#----update------

persone = {
    "Nome" : "Andrea",      
    "Cognome" : "Di Lallo", 
    "Eta" : 41
}
persone.update({"Nome": "Drew"})

#------aggiungere una chiave-----

persone.update({"Colore preferito": "Blu"})

#eliminare una chiave

# persone.pop("Nome")  #pop
# del persone["Nome"]  #del

###############################------CICLARE-------###########################################

persone = {
    "Nome" : "Andrea",      
    "Cognome" : "Di Lallo", 
    "Eta" : 41
}
for x in persone.keys():   # mandiamo a schermo LE CHIAVI
    print(x)

persone = {
    "Nome" : "Andrea",      
    "Cognome" : "Di Lallo", 
    "Eta" : 41
}
for x in persone.values():  #mandiamo a schermo I VALORI
    print(x)
    
##########se volessimo tutte le TUPLE

persone = {
    "Nome" : "Andrea",      
    "Cognome" : "Di Lallo", 
    "Eta" : 41
}
for x, y in persone.items():  #sono composti da 2 valori quindi la print dovrà essere fatta su x e y
    print(x, y)
    
#---------copiare-------

persone = {
    "Nome" : "Andrea",      
    "Cognome" : "Di Lallo", 
    "Eta" : 41
}

x = persone.copy()
print(x)

#-------se volessimo creare un nuovo DICT da quello esistente---

persone = {
    "Nome" : "Andrea",      
    "Cognome" : "Di Lallo", 
    "Eta" : 41
}
nuovo_dict = dict(persone)
print(nuovo_dict)

#################################---------------------DICT ANNIDATI-----------------#############################################


persone = {
    "Nome" : "Andrea",      
    "Cognome" : "Di Lallo", 
    "Eta" : 41,
    "indirizzo": {          # annidamento
        "Citta": "Roma",
        "Via": "Viale Marx",
        "Civico": "210",
        "CAP": "00137"
    }
}
print(persone)

print(persone["indirizzo"]["CAP"]) #visualizzare un valore dell'annidamento





#############################################---------FUNZIONI-----------####################################################
# sono una serie di operazioni ricorrenti che possono essere richiamate

# ESEMPIO:
## def fai_la_pasta:      !!QUESTA E' LA FUNZIONE!!

## metti l'acqua 
## fai bollire
## metti la pasta

#possiamo richiamare la funzione fatti la pasta che eseguirà tutti i passaggi in automatico

def fai_la_pasta():         # definiamo la funzione
    print("metti l'acqua")
    print("fai bollire")
    print("metti la pasta")
    
fai_la_pasta                # richiamiamo la funzione

fai_la_pasta                #anche piu volte
fai_la_pasta
fai_la_pasta                 

#---------------PARAMETRI------------

def fai_la_pasta(tipo_pasta):    #dichiariamo parametro
    print("metti l'acqua")
    print("fai bollire")
    print("metti " + tipo_pasta)  #lo inseriamo dove opportuno

fai_la_pasta("spaghetti") #assegnamo l' argomento alla funzione

#altro esempio

def fai_la_pasta(tipo_pasta):    #dichiariamo parametro
    print("metti l'acqua")
    print("fai bollire")
    print("metti " + tipo_pasta)  #lo inseriamo dove opportuno

fai_la_pasta("fusilli") #assegnamo l' argomento alla funzione

#possiamo avere piu parametri:

def fai_la_pasta(tipo_pasta, metti_sugo):    
    print("metti l'acqua")
    print("fai bollire")
    print("metti " + tipo_pasta)
    if metti_sugo:
        print("metti sugo") 

fai_la_pasta("fusilli", True) #in questo caso metti_sugo è si o no, quindi True o False ma ovviamente si possono inserire varie caratteristiche

#--------Arbitrary Arguments----------
# possiamo inserire argomenti indefiniti e infiniti:

def fai_la_pasta(*opzione):    # inseriamo asterisco e nome del parametro
    print("metti l'acqua")
    print("fai bollire")
    print("metti " + opzione[0]) # richiamiamo il parametro dove serve
    if opzione[1]:               #possiamo ciclare e richiamare altro parametro
        print("metti sugo")
    if opzione[2]:               #altro parametro ecc
        print("Impiatta")

fai_la_pasta("fusilli", True, True) #assegno tutti gli argomenti dichiarati prima


#---------Keyword Arguments-----------
#possiamo dichiarare gli argomenti con delle keyword

def fai_la_pasta(tipo_pasta, sugo):  # dichiariamo i parametri
    print("metti l'acqua")
    print("fai bollire")
    print("metti " + tipo_pasta)     # richiamiamo il parametro dove serve
    if sugo:                         #possiamo ciclare e richiamare altro parametro
        print("metti sugo")

fai_la_pasta(sugo=True, tipo_pasta="fusilli") #inseriamo i valori dei parametri direttamente qui

#----------Parametri di Default---------

def fai_la_pasta(tipo_pasta = "spaghetti", sugo = True):  # dichiariamo i parametri di default spaghetti al sugo
    print("metti l'acqua")
    print("fai bollire")
    print("metti " + tipo_pasta)
    if sugo:
        print("metti sugo")

fai_la_pasta()  #qui non serve specificare parametri e varranno fatti spaghetti al sugo

#se si vuole cambiare e fare dei fusilli in bianco:

def fai_la_pasta(tipo_pasta = "spaghetti", sugo = True): # dichiariamo i parametri di default spaghetti al sugo
    print("metti l'acqua")
    print("fai bollire")
    print("metti " + tipo_pasta)
    if sugo:
        print("metti sugo")

fai_la_pasta("fusilli", False) #qui cambiamo tipo_pasta e sugo su False, faranno fusilli in bianco

#--------return dei valori--------
# assegnare il ritorno,  la visualizzazione del risultato in situazioni dove è richiesto

def fai_somma(numero1, numero2):
    somma = numero1 + numero2
    
x = fai_somma(2, 5)
print(x)            # in questo caso il risultato è NONE

def fai_somma(numero1, numero2):
    somma = numero1 + numero2
    return somma    # indichiamo il return dei valori e quindi scriverà a schermo la somma, 7
    
x = fai_somma(2, 5)
print(x)   

##########################################################---CLASSI  E OGGETTI----###############################################




# --------------------------La classe viene utilizzata quindi come modello per creare un oggetto. 

# Ogni modello definisce attributi e metodi che possono essere utilizzati dagli oggetti creati(istanziati) a partire dalla classe.

# Mettiamo ad esempio che vogliamo rappresentare tramite una classe il cane:

# ------Come attributi potremmo definire nome e razza.
# ------Come metodi possiamo definire delle funzionalità di base, come ad esempio mangia e abbaia

class Cane:                             # ho creato la classe Cane e, 
    def __init__(self, nome, razza):    # nel metodo __init__(il costruttore) (vai a riga 1070)
        self.nome = nome                # ho definito gli attributi nome e razza
        self.razza = razza

def mangia():
    print("gnam gnam")
    
def abbaia():
    print("wouf wouf")

# -------------------------L'oggetto è un'istanza univoca di una classe ed ha accesso ai suoi attributi e metodi.
# per creare un oggetto basta indicare il nome della classe a cui si riferisce e tra le parentesi tonde passare(se ci sono) i parametri 
# che richiede il costruttore(nel nostro caso nome e razza).

# Andiamo ora a creare(istanziare) qualche oggetto di tipo Cane in Python:

class Cane:

    def __init__(self, nome, razza):
        self.nome = nome
        self.razza = razza
        
    def mangia(self):           #creo un oggetto
        print("gnam gnam")

    def abbaia(self):           #creo altro oggetto
        print("wouf wouf")

pluto = Cane("Pluto", "Alano")
totina = Cane("Totina", "Criceto")

print("{} è un {}".format(pluto.nome, pluto.razza))
print("{} è un {}".format(totina.nome, totina.razza))

pluto.abbaia()
totina.mangia()

#    OUTPUT
#    Pluto è un Alano
#    Totina è un Criceto
#    wouf wouf
#    gnam gnam

#######################################-------------------__init__--------------##########################################

# n Python, __init__, è un metodo speciale, 
# e viene chiamato automaticamente appena andiamo a creare un oggetto 
# ci permette di inizializzare gli attributi della classe.

#SINTASSI

class Automobile:
    def __init__(self, marca, colore, modello):  #Andiamo quindi ad aggiungere al nostro metodo Init() 
                                                 # i parametri  marca, colore e modello e inizializziamo i rispettivi attributi:
        print("Inizializzazione attributi")
        self.marca = marca
        self.colore = colore
        self.modello = modello
prima_macchina = Automobile("Lamborghini", "Blu", "Centenario")
print(prima_macchina.marca)
print(prima_macchina.colore)
print(prima_macchina.modello)


###############------------SELF-------------##################################################
class Automobile:
    def __init__(self):                 # Il parametro self rappresenta l'istanza dell'oggetto a cui si fa riferimento, 
                                        # ed è necessario inserirlo come primo parametro di ogni metodo definito all'interno di una classe.
        print("Inizializzazione classe")

prima_macchina = Automobile()

#####################################---------EREDITARIETA'--------#########################################
#è una classe --figlia-- che ha le stesse proprietà della classe --madre--

class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        
    def saluta(self):
        print("Ciao sono " + self.nome)
        
class Insegnante(Persona):     #qui definiamo una classe ereditata dalla principale, Insegnante è comunque una persona
    pass    #------------>>>>> è una istruzione che ci dice che volendo non serve più nulla da dichiarare

persona1 = Persona("Andrea", "Di Lallo")
insegnante = Insegnante("Drew", "Excalibur")

persona1.saluta()
insegnante.saluta()     #output  Ciao sono Andrea
                        #        Ciao sono Drew
                        
                        
#--------proprietà eslusive della classe figlia

class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        
    def saluta(self):
        print("Ciao sono " + self.nome)
        
class Insegnante(Persona):
    def __init__(self, nome, cognome, materia):  #dichiariamo qui il parametro esclusivo, caratterizzante
        super().__init__(nome, cognome) #-------> super viene messo in automatico e eredita automaticamente i parametri della classe super, la classe madre
        self.materia = materia #----------------> qui lo inizializziamo
       
insegnante1 = Insegnante("Drew", "Excalibur", "Astronomia")
print(insegnante1.materia)


class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        
    def saluta(self):
        print("Ciao sono " + self.nome)
        
###########-------------OVERRIDING-----------
        
class Insegnante(Persona):
    def __init__(self, nome, cognome, materia):
        super().__init__(nome, cognome)
        self.materia = materia
    
    def saluta(self): #--------------------------> override del saluta che è stato dichiarato in Persona, ora saluta da Insegnante
        print("Buongiorno sono l'insegnante " + self.nome + " " + self.cognome)
                                                           #^^^ spazio!
insegnante1 = Insegnante("Drew", "Excalibur", "Astronomia")

insegnante1.saluta() # output Buongiorno sono l'insegnante Drew Excalibur

########--------possiamo aggiungere metodi caratterizzanti che non abbiamo eritato:

class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        
    def saluta(self):
        print("Ciao sono " + self.nome)
        
class Insegnante(Persona):
    def __init__(self, nome, cognome, materia):
        super().__init__(nome, cognome)
        self.materia = materia
    
    def saluta(self):
        print("Buongiorno sono l'insegnante " + self.nome + " " + self.cognome)
                                                           #^^^ spazio!
                                                           
    def dai_voto(self): #-----------------aggiungo un metodo che potrebbe appartenere solo a questa classe ereditata
        print("Hai preso 7")
        
insegnante1 = Insegnante("Drew", "Excalibur", "Astronomia")

insegnante1.dai_voto()

#########################################---------------SCOPE delle variabili--------------------#########################################

# indica la parte di codice dove la variabile è disponibile

#----scope locale-------

def funzione():
    x = 400
    print(x)
funzione()     #in questo caso x è disponibile solo dentro la funzione, se applicassimo dopo un'altra istruzione, non funzionerebbe
                # tipo se inserissimo print(x) ci darebbe errore perchè risulterebbe non definita
                
#----scope globale------

x = 400 #-----------> dichiaro x all'inizio

def funzione():
    global x #------> uso il valore di x, globale
funzione()

#------oppure-------

x = 400 

def funzione():
    print(x)
    
funzione()



#########################################------------------MODULI--------------------####################################################
# è come se fosse una libreria, che contiene funzioni variali ecc. da usare nelle nostre applicazioni

import miomoduloprova_funzione #ho creato un file python con dentro una funzione, si chiama miomoduloprova

miomoduloprova_funzione.saluta("Andrea") #mentre si digita python ti indica già quello che è dentro al modulo

# ora utilizziamo un modulo con una variabile

import miomoduloprova_variabile

x = miomoduloprova_variabile.persona1["nome"]
print(x)
    
##-----alias dei moduli----possiamo assegnare un altro nome al modulo, più breve per comodita (3 caratteri)

import miomoduloprova_variabile as mmv #-----
#                                           |
x = mmv.persona1["nome"]# <------------------
print(x)

#############-------------------MODULI INCLUSI IN PYTHON-----------------############

#----platform

import platform
x = platform.system()
print(x)

# ce ne sono tanti §VEDERLI!!

    