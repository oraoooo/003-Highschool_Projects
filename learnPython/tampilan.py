#Tampilan Interface : Listbox, Radiobuttton, Progressbar
#Photo image, Scale
from tkinter import Tk, Listbox, Radiobutton, IntVar, PhotoImage, Label
from tkinter.ttk import Progressbar, Scale

window= Tk()

window.configure(bg="yellow")
window.geometry("1000x800")
window.resizable(False, False)


#Listbox
listbox = Listbox (window, width=10, height=10, bg="blue")
listbox.insert(1, "Pilihan 1")
listbox.insert(2, "Pilihan 2")
listbox.insert(3, "Pilihan 3")
listbox.pack()

#Radiobutton
v = IntVar()
Radiobutton(window, text="Pilihan 1", variable=v, value=1).pack()
Radiobutton(window, text="Pilihan 2", variable=v, value=2).pack()
Radiobutton(window, text="Pilihan 3", variable=v, value=3).pack()

#PhotoImage: Menampilkan gmabar
gambar = PhotoImage(file="dadu2.png")
label = Label (window, image=gambar, width=200, height=200)
label.pack()

#Progressbar
progress_bar = Progressbar(window, orient="horizontal", length=200, mode="determinate")
progress_bar.pack(pady=10)
progress_bar ["value"]=40


progress_bar = Progressbar(window, orient="vertical", length=200, mode="determinate")
progress_bar.pack()
progress_bar ["value"]=80

slider = Scale(window, from_=1, to=100, orient="horizontal")
slider.pack()

window.mainloop ()