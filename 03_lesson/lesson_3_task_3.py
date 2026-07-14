from address import Address
from mailing import Mailing

to_address = Address("Россия", "Москва", "Тверская", 10, 5)
from_address = Address("Россия", "Йошкар-Ола", "Советская", 45, 128)

mailing = Mailing(to_address, from_address, 150.50, "RU123456789")

print(f"Отправление {mailing.track} из {mailing.from_address.city} "
      f"в {mailing.to_address.city}.")
print(f"Стоимость: {mailing.cost} руб.")
