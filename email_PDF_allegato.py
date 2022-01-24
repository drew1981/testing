
import smtplib
import imghdr
from email.message import EmailMessage
import csv

Sender_Email = "test.andreadilallo@gmail.com"
#Reciever_Email = "test.andreadilallo@gmail.com"
Password = input('Inserisci la password del tuo account: ')

CSVFILE = "recipients.csv"
csvfile  = open(CSVFILE, "r")
csv_reader = csv.DictReader(csvfile)

for row in csv_reader:
    
    Cognome = row["Cognome"]
    Nome = row ["Nome"]
    email = row["Email"]
    #id = row["ID"] #da utilizzare per i PDF....da provare
    recipient = "\"" + Nome + " " + Cognome + "\" " + "<" + email + ">"
    
    print("Sto inviando email a " + email)
    mssg = mssg.replace("$NAME$", Nome + " " + Cognome)
    #mssg = mssg.replace("$SENDER$", SENDER)
    #mssg = mssg.replace("$RECIPIENT$", recipient)
    #mssg = mssg.replace("$EMAIL$",email)
    #mssg = mssg.replace("$ID$", id)

newMessage = EmailMessage()                         
newMessage['Subject'] = "Test invio Attestato" 
newMessage['From'] = Sender_Email                   
newMessage['To'] = email                   
newMessage.set_content(mssg) 

files = ['esempio_PDF.pdf']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name
    newMessage.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login(Sender_Email, Password)              
    smtp.send_message(newMessage) 