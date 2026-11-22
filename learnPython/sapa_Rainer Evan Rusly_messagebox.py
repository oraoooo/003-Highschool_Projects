#Pemogramam : Rainer Evan Rusly / XI-4 / 26 / TIK3
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.configure(bg="white")
window.geometry("1000x800")
window.resizable(False, False)
window.title("Sapa Dia!")

FIRST_NAME = tk.StringVar()
LAST_NAME = tk.StringVar()

def click_button():
    pesan = f"Halo {FIRST_NAME.get()} {LAST_NAME.get()}, Bos Gantengsss!!!!"
    showinfo(title="apa kabarrr boss!", message=pesan)

input_frame = tk.Frame(window)
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

first_name_label = ttk.Label(input_frame, text="Nama Depan: ")
first_name_label.pack(padx=10, fill="x", expand=True)

first_name_entry = ttk.Entry(input_frame, textvariable=FIRST_NAME)
first_name_entry.pack(padx=10, fill="x", expand=True)

last_name_label = ttk.Label(input_frame, text="Nama Belakang: ")
last_name_label.pack(padx=10, fill="x", expand=True)

last_name_entry = ttk.Entry(input_frame, textvariable=LAST_NAME)
last_name_entry.pack(padx=10, fill="x", expand=True)

sapa_button = ttk.Button(input_frame, text="Sapa Aja Kuy", command=click_button)
sapa_button.pack(padx=10, pady=10, fill="x", expand=True)

window.mainloop()