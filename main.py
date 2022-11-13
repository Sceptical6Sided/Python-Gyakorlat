from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import os
import internals
import random
import atexit

master = Tk()

carslist = [internals.Car("Toyota", "Corola", "black", 152, 4), internals.Car("Honda", "Civic", "white", 158, 5),
            internals.Car("Subaru", "Outback", "navy", 182, 5), internals.Car("Nissan", "Altima", "red", 188, 4),
            internals.Car("Ford", "Escape", "aqua", 250, 5), internals.Car("Honda", "Accord", "grey", 192, 4),
            internals.Car("Subaru", "Crosstrek", "grey", 182, 5), internals.Car("Mazda", "CX-5", "white", 256, 5),
            internals.Car("Hyundai", "Tucson", "black", 261, 5), internals.Car("Nissan", "Rogue", "white", 201, 5),
            internals.Car("Tesla", "Model 3", "blue", 283, 4), internals.Car("Jeep", "Wrangler", "green", 285, 5)]

filters = ["Maker", "Model", "Color", "Horsepower", "Number of seats"]

cars = {}
for c in carslist:
    cars[c] = 0


if os.path.exists("sales.txt"):
    file = open("sales.txt", "r+")

    for f in file:
        print(f.split(':')[1])
    file.close()

currentcar = StringVar()
currentfilter = StringVar()


def buycar():
    msg_box = askyesno("Are you sure", f"Are you sure you want to buy this car: {currentcar.get()}")
    if msg_box and currentcar.get() in cars:
        cars[currentcar.get()] += 1
        print(f"{currentcar.get()} {cars.get(currentcar.get())}")


def exit_handler():
    file = open("sales.txt", "w")
    for key, value in cars.items():
        file.write('%s:%s\n' % (key, value))


labelcar = Label(master, text="Select a car:")
labelcar.grid(row=0, column=0)

comboboxcar = Combobox(master, values=carslist, textvariable=currentcar)
comboboxcar.grid(row=0, column=1)

labelfilter = Label(master, text="Filter cars by:")
labelfilter.grid(row=1, column=0)

comboboxfilter = Combobox(master, values=filters, textvariable=currentfilter)
comboboxfilter.grid(row=1, column=1)

buybutton = Button(master, text="Buy selected car", command=buycar)
buybutton.grid(row=3, columnspan=2)

# ellenőrzésre használt függvény
print(carslist[random.randint(0, carslist.__len__()-1)])
mainloop()
atexit.register(exit_handler)
