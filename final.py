# قائمة المنتجات
products = [
    {"name": " طلاء الأظافر", "price": 10},
    {"name": " فرشاة لشعر", "price": 20},
    {"name": "سماعة بلوتوث ", "price": 500},
    {"name": "ماكينة تحضير القهوة", "price": 299},
    {"name": "تمثال الاوركا", "price": 350}
]

tax_rate = 0.10

product_name = input("أدخل اسم المنتج لحساب سعره مع الضريبة: ")

product_found = False
for product in products:
    if product["name"] == product_name:
        price_with_tax = product["price"] * (1 + tax_rate)
        print(f"السعر النهائي لـ {product['name']} بعد الضريبة هو: {price_with_tax:.2f} ريال")
        product_found = True
        break

if not product_found:
    print("المنتج غير موجود في القائمة.")
