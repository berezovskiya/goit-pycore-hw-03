import random


def get_numbers_ticket(min_val, max_val, quantity):

    # Генерує набір унікальних та відсортованих випадкових чисел для лотереї.
    # min_val (int): Мінімальне число (>= 1).
    # max_val (int): Максимальне число (<= 1000).
    # quantity (int): Кількість чисел для вибору.
    # Returns:
    # list: Відсортований список унікальних чисел або пустий список при невалідних даних.
    # 1. Перевірка валідності вхідних даних
    # - min має бути >= 1
    # - max має бути <= 1000
    # - quantity має бути в межах від 1 до (max - min + 1)

    if not (1 <= min_val <= max_val <= 1000) or not (0 < quantity <= (max_val - min_val + 1)):
        return "Ви ввели некоретні дані. Доступний діапазон від 1 до 1000."

    # 2. Генерація числен
    # random.sample забезпечить унікальність кожного числа в наборі
    try:
        numbers = random.sample(range(min_val, max_val + 1), quantity)
        # 3. Повернення відсортованого списку
        return sorted(numbers)
    except (ValueError, TypeError):
        # Додаткова перевірка при некоректних даних на інпуті
        return []


# Приклад використання:
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
