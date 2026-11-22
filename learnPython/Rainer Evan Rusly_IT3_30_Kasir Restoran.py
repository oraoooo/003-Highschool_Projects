import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Kasir Restoran")

menu_items = ["Burger", "Pizza", "Pasta", "Orange Juice", "Mineral Water"]
keranjang = []

judul = tk.Label(root, text="Kasir Restoran Rainer Evan Rusly XI-4/26", bg="gray", fg="green", font=("Arial", 16, "bold"))
judul.grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(root, text="Silahkan Pilih Menu").grid(row=1, column=0, sticky='w')
combo_menu = ttk.Combobox(root, values=menu_items)
combo_menu.grid(row=1, column=1)
combo_menu.set(menu_items[0])

tk.Label(root, text="Harga").grid(row=2, column=0, sticky='w')
entry_harga = tk.Entry(root)
entry_harga.grid(row=2, column=1)

tk.Label(root, text="Jumlah").grid(row=3, column=0, sticky='w')
entry_jumlah = tk.Entry(root)
entry_jumlah.grid(row=3, column=1)

def tambah_ke_keranjang():
    menu = combo_menu.get()
    harga = entry_harga.get()
    jumlah = entry_jumlah.get()

    if not harga.isdigit() or not jumlah.isdigit():
        messagebox.showerror("Error", "Harga dan Jumlah harus dalam angka")
        return

    total = int(harga) * int(jumlah)
    item = f"{menu} x{jumlah} = {total}"
    keranjang.append((menu, int(harga), int(jumlah), total))
    listbox_keranjang.insert(tk.END, item)

btn_tambah = tk.Button(root, text="TAMBAH KE KERANJANG", bg="green", fg="pink", command=tambah_ke_keranjang)
btn_tambah.grid(row=4, column=0, columnspan=2, pady=5)

tk.Label(root, text="Keranjang Belanja").grid(row=5, column=0, sticky='w')
listbox_keranjang = tk.Listbox(root, width=40, height=8)
listbox_keranjang.grid(row=6, column=0, columnspan=2)

def hapus_item():
    selected = listbox_keranjang.curselection()
    if selected:
        index = selected[0]
        listbox_keranjang.delete(index)
        del keranjang[index]
    else:
        messagebox.showwarning("Peringatan", "Pilih item yang ingin dihapus!")

btn_hapus_item = tk.Button(root, text="HAPUS ITEM", bg="orange", command=hapus_item)
btn_hapus_item.grid(row=7, column=0, columnspan=2, pady=5)

tk.Label(root, text="Diskon (%)").grid(row=8, column=0, sticky='w')
entry_diskon = tk.Entry(root, state='readonly')
entry_diskon.grid(row=8, column=1)

tk.Label(root, text="Nilai Diskon").grid(row=9, column=0, sticky='w')
entry_nilai_diskon = tk.Entry(root)
entry_nilai_diskon.grid(row=9, column=1)

tk.Label(root, text="Total Pembelian").grid(row=10, column=0, sticky='w')
entry_total = tk.Entry(root)
entry_total.grid(row=10, column=1)

tk.Label(root, text="Pajak (10%)").grid(row=11, column=0, sticky='w')
entry_pajak = tk.Entry(root)
entry_pajak.grid(row=11, column=1)

tk.Label(root, text="Tip (5%)").grid(row=12, column=0, sticky='w')
entry_tip = tk.Entry(root)
entry_tip.grid(row=12, column=1)

tk.Label(root, text="Total Pembayaran").grid(row=13, column=0, sticky='w')
entry_total_pembayaran = tk.Entry(root)
entry_total_pembayaran.grid(row=13, column=1)

def hitung_total():
    subtotal = sum(item[3] for item in keranjang)
    total_jumlah = sum(item[2] for item in keranjang)

    if total_jumlah <= 5:
        diskon_persen = 2
    elif total_jumlah <= 10:
        diskon_persen = 5
    else:
        diskon_persen = 10

    entry_diskon.config(state='normal')
    entry_diskon.delete(0, tk.END)
    entry_diskon.insert(0, str(diskon_persen))
    entry_diskon.config(state='readonly')

    nilai_diskon = subtotal * diskon_persen / 100
    total_setelah_diskon = subtotal - nilai_diskon
    pajak = total_setelah_diskon * 0.10
    tip = total_setelah_diskon * 0.05
    total_bayar = total_setelah_diskon + pajak + tip

    entry_nilai_diskon.delete(0, tk.END)
    entry_nilai_diskon.insert(0, f"{nilai_diskon:.0f}")
    entry_total.delete(0, tk.END)
    entry_total.insert(0, f"{total_setelah_diskon:.0f}")
    entry_pajak.delete(0, tk.END)
    entry_pajak.insert(0, f"{pajak:.0f}")
    entry_tip.delete(0, tk.END)
    entry_tip.insert(0, f"{tip:.0f}")
    entry_total_pembayaran.delete(0, tk.END)
    entry_total_pembayaran.insert(0, f"{total_bayar:.0f}")

def hapus_perhitungan():
    entry_diskon.config(state='normal')
    entry_diskon.delete(0, tk.END)
    entry_diskon.config(state='readonly')
    entry_nilai_diskon.delete(0, tk.END)
    entry_total.delete(0, tk.END)
    entry_pajak.delete(0, tk.END)
    entry_tip.delete(0, tk.END)
    entry_total_pembayaran.delete(0, tk.END)

btn_hitung = tk.Button(root, text="HITUNG", bg="green", fg="pink", command=hitung_total)
btn_hitung.grid(row=14, column=0, pady=5)

btn_reset = tk.Button(root, text="HAPUS", bg="red", fg="pink", command=hapus_perhitungan)
btn_reset.grid(row=14, column=1, pady=5)

def cetak_struk():
    if not keranjang:
        messagebox.showinfo("Struk", "Belum ada belanjaan.")
        return

    struk = "=== STRUK PEMBELIAN ===\n"
    for item in keranjang:
        struk += f"{item[0]} x{item[2]} = {item[3]}\n"
    struk += f"\nDiskon: {entry_diskon.get()}%\n"
    struk += f"Total Bayar: Rp {entry_total_pembayaran.get()}"

    messagebox.showinfo("Struk Belanja", struk)

btn_struk = tk.Button(root, text="CETAK STRUK", bg="purple", fg="pink", command=cetak_struk)
btn_struk.grid(row=15, column=0, columnspan=2, pady=5)

root.mainloop()