def calculate_pizza(ingredients):
    price = sum(item['price'] for item in ingredients)
    calories = sum(item['calories'] for item in ingredients)
    return calories, price
