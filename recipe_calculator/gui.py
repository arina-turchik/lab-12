import tkinter as tk
from tkinter import messagebox
from .recipes import recipes
from .calculations import calculate_energy_value, calculate_cost

def create_gui():
    root = tk.Tk
    root.title = ("Рецепты")

#эл. интерфейса, выбор рецепта и параметры

def calculate():
    #рассчёт выбранного рецепта
    energy_value = calculate_energy_value(selected_ingridients)
    cost = calculate_cost(selected_ingridients)

massaebox_showinfo("Результаты", f"Энергитечская ценность: {energy_value} \n Стоимость: {cost}")


calculate_button = tk.Button(root, text = "Рассчитать", command = calculate)
calculate_button.pack()

root.mainloop()
