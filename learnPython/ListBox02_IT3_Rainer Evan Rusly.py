import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import ttk

root = tk.Tk()
root.geometry('400x250')
root.title('Listbox')

kelas = ('IT 1', 'IT 2', 'IT 3', 'IT 4')
nomor = ('1', '2', '3', '4', '5', '6')

kelas_variable = tk.Variable(value=kelas)
nomor_variable = tk.Variable(value=nomor)

kelas_label = ttk.Label(root, text='Pilih kelas Anda:')
kelas_label.pack(padx=10, pady=5, anchor='w')

kelas_listbox = tk.Listbox(
    root,
    listvariable=kelas_variable,
    height=4,
    selectmode=tk.SINGLE,
    exportselection=False 
)
kelas_listbox.pack(padx=10, pady=5, side=tk.LEFT, expand=True, fill=tk.BOTH)

nomor_label = ttk.Label(root, text='Pilih nomor Anda:')
nomor_label.pack(padx=10, pady=5, anchor='w')

nomor_listbox = tk.Listbox(
    root,
    listvariable=nomor_variable,
    height=6,
    selectmode=tk.SINGLE,
    exportselection=False
)
nomor_listbox.pack(padx=10, pady=5, side=tk.LEFT, expand=True, fill=tk.BOTH)

def handle_item_select(event):
    selected_kelas_index = kelas_listbox.curselection()
    selected_nomor_index = nomor_listbox.curselection()
    
    if selected_kelas_index and selected_nomor_index:
        selected_kelas = kelas_listbox.get(selected_kelas_index)
        selected_nomor = nomor_listbox.get(selected_nomor_index)
        
        showinfo(
            title='Informasi',
            message=f'Saya di kelas {selected_kelas}, nomor {selected_nomor}'
        )

kelas_listbox.bind('<<ListboxSelect>>', handle_item_select)
nomor_listbox.bind('<<ListboxSelect>>', handle_item_select)

root.mainloop()