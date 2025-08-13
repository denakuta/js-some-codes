products = {
    'apple': 1123,
    'milk': 89,
    'bread': 45,
    'cheese': 650,
    'eggs': 120,
    'chicken': 250,
    'rice': 95,
    'potatoes': 30,
    'tomatoes': 180,
    'bananas': 99,
    'orange': 85,
    'yogurt': 65,
    'pasta': 75,
    'onions': 25,
    'carrots': 35,
    'beef': 320,
    'fish': 280,
    'cookies': 150
}

def discount(data_price):
    price = data_price.get(input('Введите название товара: '))
    discountprice = float(input('Введите размер скидки: ')) / 100
    return int(price * (1 - discountprice))


print(discount(products), 'рублей')
