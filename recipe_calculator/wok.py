def calculate_wok(ingredients):
    price = sum(item['price'] for item in ingredients)
    calories = sum(item['calories'] for item in ingredients)
    return calories, price
