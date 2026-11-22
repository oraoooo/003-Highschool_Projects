import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Program Temperatur oleh Rainer Evan Rusly')

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

c_value = tk.DoubleVar()
k_value = tk.DoubleVar()

def get_c_value():
    return '{: .2f}'.format(c_value.get())
def get_k_value():
    return '{: .2f}'.format(k_value.get())

def c_slider_changed(event):
    c_output.configure(text=get_c_value())
    k_value.set(c_value.get()+273.15)
    k_output.configure(text=get_k_value())
    
def k_slider_changed(event):
    k_output.configure(text=get_k_value())
    c_value.set(k_value.get()-273.15)
    c_output.configure(text=get_c_value())

c_slider_label = ttk.Label(
    root,
    text='Celcius :'
)
c_slider_label.grid(
    row=0,
    column=0,
    sticky='we',
)

# Membuat c_slider
c_slider = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',
    command=c_slider_changed,
    variable=c_value
)
c_slider.grid(
    row=0,
    column=1,
)

c_value_label = ttk.Label(
    root,
    text='Suhu sekarang dalam Celsius:'
)
c_value_label.grid(
    row=1,
    columnspan=2,
    sticky='n',
    ipadx=10,
    ipady=10,
)
c_output = ttk.Label(
    root,
    text=get_c_value()
)
c_output.grid(
    row=2,
    columnspan=2,
    sticky="n"
)


k_slider_label = ttk.Label(
    root,
    text='Kelvin :'
)
k_slider_label.grid(
    row=3,
    column=0,
    sticky='we',
)

# Membuat k_slider
k_slider = ttk.Scale(
    root,
    from_=273.15,
    to=373.15,
    orient='horizontal',
    command=k_slider_changed,
    variable=k_value
)
k_slider.grid(
    row=3,
    column=1,
)

k_value_label = ttk.Label(
    root,
    text='Suhu sekarang dalam Kelvin:'
)
k_value_label.grid(
    row=4,
    columnspan=2,
    sticky='n',
    ipadx=10,
    ipady=10,
)
k_output = ttk.Label(
    root,
    text=get_k_value()
)
k_output.grid(
    row=5,
    columnspan=2,
    sticky="n"
)


root.mainloop()