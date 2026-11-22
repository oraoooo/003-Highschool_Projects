#dibuat oleh Rainer Evan Rusly IT3

import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Form Lomba")
window.geometry("500x200")

frame1 = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=1)
frame1.pack(side=tk.LEFT, fill=tk.Y)

frame2 = tk.Frame(master=window, relief=tk.RIDGE)
frame2.pack(side=tk.RIGHT)

list = {
    0: 'No. Pendaftaran',
    1: 'Nama Lengkap',
    2: 'Asal Sekolah',
    3: 'Alamat Sekolah',
    4: 'Lomba',
}

entries = {}
jenis_lomba = tk.IntVar()

for i in range(5):
    label = tk.Label(master=frame1, text= list[i]+':')
    label.grid(row=i, column=0, sticky=tk.W)
    
    entry=tk.Entry(master=frame2, width=50)
    entry.grid(row=i, column=1, sticky=tk.W)
    entries[i] = entry

label_jl = tk.Label(master=frame1)
label_jl['text'] =  'Jenis Lomba :'
label_jl.grid(row=10, column=0, sticky=tk.W)

entry_jl1 = tk.Radiobutton(master=frame2, text='Individu', variable=jenis_lomba, value=1)
entry_jl1.grid(row=10, column=0, sticky=tk.W)

entry_jl2 = tk.Radiobutton(master=frame2, text='Group', variable=jenis_lomba, value=2)
entry_jl2.grid(row=10, column=1, sticky=tk.W)

def submit():
    messagebox.showinfo("Sukses", "Data siswa berhasil disimpan")

def clear():
    for entry in entries.values():
        entry.delete(0, tk.END)
    jenis_lomba.set(0)

button1 = tk.Button(master=frame2, text='Submit', command=submit)
button1.grid(row=11, column=0, sticky=tk.W)

button2 = tk.Button(master=frame2, text='Cancel', command=clear)
button2.grid(row=11, column=1, sticky=tk.W)

window.mainloop()