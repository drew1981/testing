import tkinter as tk
import PyPDF2
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo
import pathlib


window=tk.Tk()
window.title("PDF a TESTO")
window.geometry("500x50+500+400")

def openfile():
    file=askopenfile(filetypes=[('PDF Files','*.pdf')])
    pdf_file=open(file.name,'rb')
    read_pdf=PyPDF2.PdfFileReader(pdf_file)
    no_of_pages=read_pdf.getNumPages()
    page=read_pdf.getPage(0)
    page_content=page.extractText()
    pathlib.Path('context.txt').write_text(page_content)
    showinfo("Fatto","PDF Convertito")
    
label=tk.Label(window,text="Scegli File PDF: ")
label.grid(row=0,column=0,padx=5,pady=5)

button=ttk.Button(window,text="Seleziona",width=30,command=openfile)
button.grid(row=0,column=1,padx=5,pady=5)

window.mainloop()