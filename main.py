from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import os
import internals
import random
import atexit

master = Tk()
master.title("Car shop")
master.geometry("250x100")

cars_list = [internals.Car("Toyota", "Corola", "black", 152, 4), internals.Car("Honda", "Civic", "white", 158, 5),
             internals.Car("Subaru", "Outback", "navy", 182, 5), internals.Car("Nissan", "Altima", "red", 188, 4),
             internals.Car("Ford", "Escape", "aqua", 250, 5), internals.Car("Honda", "Accord", "grey", 192, 4),
             internals.Car("Subaru", "Crosstrek", "grey", 182, 5), internals.Car("Mazda", "CX-5", "white", 256, 5),
             internals.Car("Hyundai", "Tucson", "black", 261, 5), internals.Car("Nissan", "Rogue", "white", 201, 5),
             internals.Car("Tesla", "Model 3", "blue", 283, 4), internals.Car("Jeep", "Wrangler", "green", 285, 5)]

cars = {}
for c in cars_list:
    cars[c] = 0


if os.path.exists("sales.txt"):
    file = open("sales.txt", "r+")

    for f in file:
        print(f.split(':')[1])
    file.close()

current_car = StringVar()


def buy_car():
    msg_box = askyesno("Are you sure", f"Are you sure you want to buy this car: {current_car.get()}")
    if msg_box and current_car.get() in cars:
        cars[current_car.get()] += 1
        print(f"{current_car.get()} {cars.get(current_car.get())}")


def exit_handler():
    file = open("sales.txt", "w")
    for key, value in cars.items():
        file.write('%s:%s\n' % (key, value))


def car_selection_changed():
    label_selected_car.config(text=f"Your selected car is:{current_car.get()}")
    label_selected_car.grid(row=2, columnspan=2)


label_car = Label(master, text="Select a car:")
label_car.grid(row=0, column=0)

combobox_car = Combobox(master, values=cars_list, textvariable=current_car)
combobox_car.grid(row=0, column=1)
combobox_car.bind("<<ComboboxSelected>>", car_selection_changed)

label_selected_car = Label(master)

buy_button = Button(master, text="Buy selected car", command=buy_car)
buy_button.grid(row=3, columnspan=2)

print(cars_list[random.randint(0, cars_list.__len__() - 1)])

mainloop()
atexit.register(exit_handler)
