products = [
    {"name":  "طلاء اظافر", "price": 10},
    {"name": "فرشاة شعر", "price": 20},
    {"name": "سماعة بلوتوث", "price": 500},
    {"name": "ماكينة تحضير القهوة", "price": 299},
    {"name": "تمثال حوت الاوركا ", "price": 350}
]

tax_rate = 0.10

for product in products:
    price_with_tax = product["price"] * (1 + tax_rate)
    print(f"السعر النهائي لـ {product['name']} بعد الضريبة هو: {price_with_tax:.2f} ريال")

