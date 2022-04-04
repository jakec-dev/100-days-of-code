from tkinter import Button, Label, Entry, Tk

window = Tk()
window.title("Miles to Kilometres converter")
window.config(padx=20, pady=20)


def button_on_click():
    miles_value = int(entry.get())
    km_value = miles_value * 1.6
    result.config(text=km_value)


calc_button = Button(text="Calculate", command=button_on_click)
calc_button.grid(column=1, row=2)

entry = Entry(width=10)
entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=0, row=1)

result = Label(text="0")
result.grid(column=1, row=1)

window.mainloop()
