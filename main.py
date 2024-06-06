from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=200)
window.config(padx=40, pady=40)


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result.config(text=f"{km}")


miles_input = Entry()
miles_input.grid(column=1, row=0)

is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

km_result = Label()
km_result.grid(column=1, row=1)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

km = Label(text="Km")
km.grid(column=2, row=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()
