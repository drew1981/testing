import tkinter as tk
from tkinter.filedialog import askopenfilename
from PyPDF2 import PdfFileMerger, PdfFileReader
from pathlib import Path
from tkinter import *

filelist = []

# initiate merger Object
merger = PdfFileMerger()

def open_file(files):
    filepath = askopenfilename(
        filetypes=[("PDF Files","*.pdf"), ("All Files", "*.*")]
    )
    if not(filepath and Path(filepath).exists()):
        return
    files.append(filepath)
    # list out all filenames
    lbl_items["text"] = '\n'.join(str(f) for f in files)
    if len(files) >= 2 and btn_merge['state'] == "disabled":
        btn_merge["state"] = "normal"

def merge_pdfs(files):
    for f in files:
        merger.append(PdfFileReader(open(f, "rb")))
    
    output_filename = ent_output_name.get()

    if not output_filename:
        output_filename = "Untitled.pdf"
    elif ".pdf" not in output_filename:
        output_filename += ".pdf"
    merger.write(output_filename)

# create desktop GUI
window = tk.Tk()
window.title("PDFMerger Tk")
window.geometry("900x500+200+100")
# not allowed resizing x y direction
window.resizable(0,0)


#aggiungo immagine di sfondo
bg = PhotoImage(file = "pdfmergerADL.png")
  
#imposto immagine di sfondo come un label
label1 = Label(window, image=bg)
label1.place(relx=0, rely=0)

# --- Ask open files ---
#fr_bg1 = tk.Frame(window, bd=3)
#lbl_open = tk.Label(fr_bg1, text="Please choose PDFs to join: (2 and above)")
#lbl_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

btn_open = tk.Button(window, text="Apri 2 o più PDF", width=50, height=2, activebackground="#27dc74",
                command=lambda: open_file(filelist))
btn_open.place(x=220, y=200)
lbl_items = tk.Label(window, text="", width=50, bg="white")
lbl_items.place(x=235, y=280)
#fr_bg1.pack()

etichetta_nome = tk.Label(window, text="Inserisci il nome del PDF che verrà creato", width=40, bg="white")
etichetta_nome.place(x=280, y=320)
# --- Button to merge PDFs ---
#fr_bg2 = tk.Frame(window, bd=3)
#lbl_to_merge = tk.Label(fr_bg2, text="Merge selected files (in PDF)")
#lbl_to_merge.grid(row=0, column=0, sticky="ew", padx="5", pady="5")

ent_output_name = tk.Entry(window, width=20)
ent_output_name.place(x=370, y=340)

btn_merge = tk.Button(window, 
                text="Merge PDF", activebackground="#dc9927", width=50, height=2,
                state="disabled",
                command=lambda: merge_pdfs(filelist))
btn_merge.place(x=220, y=400)
#fr_bg2.pack()

# --- Button to exit ---
#btn_exit = tk.Button(window, text="Exit", command=window.destroy, bd=2)
#btn_exit.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.FALSE)

if __name__ == "__main__":
    window.mainloop()
