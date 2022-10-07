import re

regex = "^(\+549|\(?0?)(345)\)?\s?((15)?\d{7})$"

phone_1 = "(0345) 154123456"
phone_2 = "+5493454123456"
phone_3 = "3454123456"
phone_4 = "+54011123456"
phone_5 = "34564123456"


def is_valid_phone(phone: str) -> bool:
    return bool(re.search(regex, phone, flags=0))

print("Es de Concordia?", is_valid_phone(phone_1))
print("Es de Concordia?", is_valid_phone(phone_2))
print("Es de Concordia?", is_valid_phone(phone_3))
print("Es de Concordia?", is_valid_phone(phone_4))
print("Es de Concordia?", is_valid_phone(phone_5))