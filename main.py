purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

# Рассчет и возврат общей выручки (цена * количество для всех записей)
def total_revenue(purchases):
    total_rev = sum(item["price"] * item["quantity"] for item in purchases)
    return print(f"Общая выручка: {total_rev}")

# Возврат словаря, где ключ — категория, а значение — список уникальных товаров в этой категории
def items_by_category(purchases):
    items_by_cat = {}
    for purchase in purchases:
        category = purchase["category"]
        if category not in items_by_cat:
            items_by_cat[category] = []
        if purchase["item"] not in items_by_cat[category]:
            items_by_cat[category].append(purchase["item"])
    return print(f"Товары по категориям: {items_by_category}")

# Вывод всех покупок, где цена товара больше или равна min_price
def expensive_purchases(purchases, min_price):
    expensive_pur = []
    for item in expensive_pur:
        if item["price"] >= min_price:
            expensive_pur.append(item)
    return print(f"Покупки дороже {min_price}: {expensive_pur}")

# Рассчет средней цены товаров по каждой категории
def average_price_by_category(purchases):
    category_prices = {}
    for purchase in purchases:
        category = purchase["category"]
        if category not in category_prices:
            category_prices[category] = []
        category_prices[category].append(purchase["price"])
    averages_by_category = {}
    for category, prices in category_prices.items():
        averages_by_category[category] = sum(prices) / len(prices)
    return print(f"Средняя цена по категориям: {averages_by_category}")

# Вывод категорию, в которой куплено больше всего единиц товаров (учитывается по полю quantity)
def most_frequent_category(purchases):
    category_quantities = {}
    for item in purchases:
        category = item["category"]
        if category not in category_quantities:
            category_quantities[category] = 0
        category_quantities[category] += item["quantity"]
    result = max(category_quantities, key=category_quantities.get)
    return print(f"Категория с наибольшим количеством проданных товаров: {result}")


total_revenue(purchases)
items_by_category(purchases)
expensive_purchases(purchases, 1.0)
average_price_by_category(purchases)
most_frequent_category(purchases)