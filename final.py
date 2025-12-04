products = [
    {"name": "طعام افطار", "price": 10},
    {"name": "قهوة شعر", "price": 20},
    {"name": "طابعة بلوتر", "price": 500},
    {"name": "ماكينة تحضير القهوة", "price": 299},
    {"name": "تمثال حول الاوركا", "price": 350}
]

tax_rate = 0.10

for product in products:
    price_with_tax = product["price"] * (1 + tax_rate)
    print(f"أسعار النهاية لـ {product['name']} بعد الضريبة هو: {price_with_tax:.2f} ريال")
