import tkinter as tk

window = tk.Tk()
window.geometry("600x600")
window.title("Hello!")
# window.resizable(False, False)
window.configure(background="grey")


def first_print():
    text = "Hello World!"
    text_output = tk.Label(window, text=text, fg="black", font=("Helvetica", 16))
    text_output.grid(row=1, column=1, sticky="W")

def second_function():
    text = "Hello Mars"
    text_output = tk.Label(window, text=text, fg="green", font=("Helvetica", 16))
    text_output.grid(row=4, column=1, padx=50, sticky="W")

first_button = tk.Button(text="SALUTO", command=first_print)
first_button.grid(row=4, column=0, sticky="W")

second_button = tk.Button(text="SALUTO MARZIANO", command=second_function)
second_button.grid(row=8, column=0, pady=20, sticky="W")


if __name__ == "__main__":
    window.mainloop()