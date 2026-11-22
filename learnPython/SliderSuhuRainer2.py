import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Program Temperatur oleh Rainer Evan Rusly')

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

c_value = tk.DoubleVar()

def get_c_value():
    return '{: .2f}'.format(c_value.get())

def get_k_value():
    return '{: .2f}'.format(c_value.get() + 273.15)

def c_slider_changed(event):
    c_output.configure(text=get_c_value())
    k_output.configure(text=get_k_value())

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
k_value_label = ttk.Label(
    root,
    text='Suhu sekarang dalam Kelvin:'
)
k_value_label.grid(
    row=3,
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
    row=4,
    columnspan=2,
    sticky="n"
)


root.mainloop()