import re

def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр
    digits = re.sub(r"\D", "", phone_number)
    
    # Беремо останні 9 цифр (наприклад, 501234567)
    # Це універсально працює для форматів 050..., 38050..., +38050...
    main_part = digits[-10:]
    return f"+38{main_part}"

# Приклад роботи функції
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)