class Recipe:
    def __init__(self, name, ingridients):
        self.name = name
        self.ingridients = ingridients

    def energy_value(self):
        #ценность
        pass

    def cost(self):
        #стоимость
        pass

recipes = [
    Recipe("Вок", {"лапша": 100, "овощи": 50, "соус": 20}),
    Recipe("Бургер", {"булочка": 50, "мясо": 150, "салат": 30})
    Recipe("Пицца", {"тесто": 200, "сыр": 100, "помидоры": 50})
]
