from PyPDF2 import PdfFileWriter, PdfFileReader
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
#from PIL import Image, ImageTk

def open_file():
  file = filedialog.askopenfilename(initialdir = "~",
                                    title = "Scegli un PDF",
                                    filetypes = [("PDF Files", "*.pdf")])
  if file != "":
    input['text'] = file
    total_pages = PdfFileReader(open(file, "rb"), strict=False).numPages
    pages = [ i  for i in range(1, total_pages+1) ]
    left_combo.config(values=pages)
    right_combo.config(values=pages)
    left_combo.current(0)
    right_combo.current(0)

def save_file():
  min = left_combo.get()
  max = right_combo.get()
  if (min != "..."):
    min = int(min) - 1
    max = int(max)
    if (min <= max):
      file = filedialog.asksaveasfile(initialdir = "~", 
                                      title = "Salva File", 
                                      filetypes = [("PDF", "*.pdf")],
                                      defaultextension=".pdf")
      pdf_reader = PdfFileReader(open(input['text'], "rb"), strict=False)
      pdf_writer = PdfFileWriter()
      for page in range(min, max):
        pdf_writer.addPage(pdf_reader.getPage(page))
      with open(file.name, 'wb') as f:
        pdf_writer.write(f)


if __name__ == '__main__':

  root = Tk()
  root.title("ADL-PDF Splitter")
  root.geometry("900x550+150+150")
  root.resizable(width=False, height=False)
  
  #aggiungo immagine di sfondo
  bg = PhotoImage(file = "pdfsplitterADL.png")
  
  #imposto immagine di sfondo come un label
  label1 = Label(root, image=bg)
  label1.place(relx=0, rely=0)
  
  
  # Creo entry + buttons
  open_file = Button(root, text="Apri File", width=50, height=2, activebackground="#27dc74", command=open_file)
  save_file = Button(root, text="Salva File", width=50, height=2, activebackground="#dc9927", command=save_file)
  input = Label(root, relief=GROOVE, width=50, text="Nessun PDF selezionato")
  #to = Label(root, text="-")
  left_combo = ttk.Combobox(root, state="readonly", values=["..."], width=10)
  right_combo = ttk.Combobox(root, state="readonly", values=["..."], width=10)

  left_combo.current(0)
  right_combo.current(0)

  # Posiziono entry + buttons
  #open_file.grid(column=2, row=2, ipadx=5, pady=5, sticky=N)
  #input.grid(column=6, row=3)
  #left_combo.grid(column=7, row=4)
  #to.grid(row=6, column=9, padx=15)
  #right_combo.grid(column=8, row=5)
  #save_file.grid(column=9, row=6)
  
  #provo ad usare .pack
  #open_file.pack(pady=200, fill=X)
  #input.pack(ipadx=100, fill=X )
  #left_combo.pack(side="left", padx=160)
  #right_combo.pack(side="right", padx=160)
  #save_file.pack(ipadx=100)
  
  #provo ad usare .place
  open_file.place(x=220, y=200)
  input.place(x=230, y=280)
  left_combo.place(x=350, y=340)
  right_combo.place(x=470, y=340)
  save_file.place(x=220, y=450)

  # Centro la finestra
  #root.eval('tk::PlaceWindow . center')

  root.mainloop()
