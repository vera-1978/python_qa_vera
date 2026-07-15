from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15", "+79991112233"),
    Smartphone("Samsung", "Galaxy S24", "+79992223344"),
    Smartphone("Xiaomi", "14 Ultra", "+79993334455"),
    Smartphone("Realme", "GT 6", "+79994445566"),
    Smartphone("Huawei", "Pura 70", "+79995556677")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.phone_number}")
