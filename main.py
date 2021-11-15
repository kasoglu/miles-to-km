from tkinter import *

# Setting Screen

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)


# Miles input area

mile = Entry(width=7)
mile.grid(column=2, row=1)

# Label areas

label_1 = Label(text="Miles")
label_1.grid(column=3, row=1)

label_2 = Label(text="is equal to")
label_2.grid(column=1, row=2)

label_3 = Label(window, text="0")
label_3.grid(column=2, row=2)


# Calculating Function and configure text as kilometers.

def miles_to_km():
    miles = float(mile.get())
    km = round(miles * 1.609)
    label_3.configure(text=str(km) + '  Km')


# Calculate button

button = Button(text="Calculate", command=miles_to_km)

button.grid(column=2, row=3)

# Looping window on screen

window.mainloop()
