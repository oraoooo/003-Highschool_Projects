import tkinter as tk
from tkinter import messagebox

def cari_zodiak():
# meminta input tanggal, bulan, dan tahun lahir dari user
    tanggal = float(entry_tanggal.get())
    bulan = float(entry_bulan.get())
    tahun = float(entry_tahun.get())
    if (bulan == 3 and tanggal >= 21) or (bulan == 4 and tanggal <= 19):
        hitung = "Aries"
        Karakter = "Berani, ambisius, cepat bergerak, suka tantangan"
    elif (bulan == 4 and tanggal >= 20) or (bulan == 5 and tanggal <= 20):
        hitung = "Taurus"
        Karakter = "Setia, sabar, mencintai kenyamanan, keras kepala"
    elif (bulan == 5 and tanggal >= 21) or (bulan == 6 and tanggal <= 20):
        hitung = "Gemini"
        Karakter = "Cerdas, komunikatif, mudah bosan, fleksibel"
    elif (bulan == 6 and tanggal >= 21) or (bulan == 7 and tanggal <= 22):
        hitung = "Cancer"
        Karakter = "Emosional, intuitif, penyayang, protektif"
    elif (bulan == 7 and tanggal >= 23) or (bulan == 8 and tanggal <= 22):
        hitung = "Leo"
        Karakter = "Percaya diri, karismatik, suka perhatian, dramatis"
    elif (bulan == 8 and tanggal >= 23) or (bulan == 9 and tanggal <= 22):
        hitung = "Virgo"
        Karakter = "Perfeksionis, analitis, suka membantu, teliti"
    elif (bulan == 9 and tanggal >= 23) or (bulan == 10 and tanggal <= 22):
        hitung = "Libra"
        Karakter = "Adil, diplomatis, cinta damai dan keindahan"
    elif (bulan == 10 and tanggal >= 23) or (bulan == 11 and tanggal <= 21):
        hitung = "Scorpio"
        Karakter = "Misterius, intens, setia, emosional"
    elif (bulan == 11 and tanggal >= 22) or (bulan == 12 and tanggal <= 21):
        hitung = "Sagittarius"
        Karakter = "Petualang, optimis, blak-blakan, cinta kebebasan"
    elif (bulan == 12 and tanggal >= 22) or (bulan == 1 and tanggal <= 19):
        hitung = "Capricorn"
        Karakter = "Ambisius, disiplin, bertanggung jawab, pekerja keras"
    elif (bulan == 1 and tanggal >= 20) or (bulan == 2 and tanggal <= 18):
        hitung = "Aquarius"
        Karakter = "Unik, visioner, mandiri, peduli kemanusiaan"
    elif (bulan == 2 and tanggal >= 19) or (bulan == 3 and tanggal <= 20):
        hitung = "Pisces"
        Karakter = "Peka, imajinatif, penyayang, spiritual"
    else:
        hitung = "Invalid tanggal"
        Karakter = "-"

    # menampilkan hasil zodiak ke user
    showinfo_label.config(text = hitung)
    Karakter_label.config(text = Karakter)
    messagebox.showinfo("Hasil", "Zodiak Kamu Adalah " + hitung)
    
    entry_tanggal.delete(0, tk.END)
    entry_bulan.delete(0, tk.END)
    entry_tahun.delete(0, tk.END)

# membuat window tkinter
window = tk.Tk()
window.title("Zodiak")
window.geometry("285x150")

# membuat label dan entry untuk tanggal, bulan, dan tahun lahir
label_tanggal = tk.Label(text="Tanggal (dd):")
label_tanggal.grid(column=0, row=1)
entry_tanggal = tk.Entry()
entry_tanggal.grid(column=1, row=1)

label_bulan = tk.Label(text="Bulan (mm):")
label_bulan.grid(column=0, row=2)

entry_bulan = tk.Entry()
entry_bulan.grid(column=1, row=2)

label_tahun = tk.Label(text="Tahun (yyyy):")
label_tahun.grid(column=0, row=3)
entry_tahun = tk.Entry()
entry_tahun.grid(column=1, row=3)

showinfo_labelawal = tk.Label(text="Zodiak:")
showinfo_labelawal.grid(column=0, row=4)

showinfo_label = tk.Label(text=".................................")
showinfo_label.grid(column=1, row=4)

sifat_labelawal = tk.Label(text="Karakter:")
sifat_labelawal.grid(column=0, row=5)

Karakter_label = tk.Label(text=".................................")
Karakter_label.grid(column=1, row=5)

button_cari_zodiak = tk.Button(text="Cari Zodiak", command=cari_zodiak)
button_cari_zodiak.grid(column=1, row=6)
window.mainloop()