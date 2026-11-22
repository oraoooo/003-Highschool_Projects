#bikinan Rainer Evan Rusly IT3

import tkinter as tk

window = tk.Tk()
window.configure(bg="yellow")
window.geometry("1000x800")
window.resizable(False, False)

window.title("Pengenalan tkinter")

def showText ():
    label3.config(text="Happy New Year")

label1 = tk.Label(window, text="Hello, Tkinter", font=("Arial", 16))
label1.pack(pady=20)

label2 = tk.Label(window, text="PROGRAMMER : RAINER EVAN RUSLY - XI-4 - 26", font=("Arial", 20))
label2.pack(pady=20)

label3 = tk.Label(window, text="", font=("Arial", 30))
label3.pack(pady=20)

button1 = tk.Button(window, text="Click Here!", bg="blue", fg="red", font=("Arial", 16), command=showText)
button1.pack()

window.mainloop()