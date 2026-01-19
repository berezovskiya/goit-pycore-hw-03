import re


def normalize_phone(phone_number):
    """
    скріпт нормалізує номер телефону: видаляє зайве, а також додає/нормалізує телефоний код України +38, якщо відсутній.

    Аргументи для функції: 
        phone_number (str): Вхідний рядок з невідформатованими для розсилки номеромами в рядковому форматі

    Вивід функції
         Нормалізований номер у форматі +380XXXXXXXXX -> в рядковому форматі
    """
    # видаляємо всі зайіві символи, тобто все, що  не є цифрами або знаком '+'
    cleaned_number = re.sub(r"[^\d+]", "", phone_number.strip())

    # перевірка та корекція кода України
    if cleaned_number.startswith("+380"):
        normalized = cleaned_number
    elif cleaned_number.startswith("380"):
        # номер має код країни, але без плюса
        normalized = "+" + cleaned_number
    else:
        # номер без коду країни (наприклад, 050...)
        normalized = "+38" + cleaned_number

    return normalized


# приклад роботи:
raw_numbers = [
    "067\t123 4567",
    "(095)    234 - 5678\n",
    "           +380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "  0503451234",
    "(050)8889900",
    "38050-1  11-22-22",
    "380  50 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для розсилки:", sanitized_numbers)
