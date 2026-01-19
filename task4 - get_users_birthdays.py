from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    """
    визначає користувачів, чий день народження відбудеться протягом наступних 7 днів,
    враховуючи вихідні дні для дати привітання.
    """
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        # 1. Конвертуємо дату народження з рядка в об'єкт date
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # 2. Визначаємо дату народження на поточний рік
        birthday_this_year = birthday.replace(year=today.year)

        # 3. Якщо день народження вже минув у цьому році, перевіряємо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(
                year=today.year + 1)

        # 4. рахуємо різницю в днях
        days_until = (birthday_this_year - today).days

        # 5. Перевіряємо, чи потрапляє дата у 7-денне вікно (включно з сьогодні)
        if 0 <= days_until <= 7:
            congratulation_date = birthday_this_year

            # 6. Перевірка на вихідні (0-понеділок, 5-субота, 6-неділя)
            weekday = congratulation_date.weekday()
            if weekday == 5:  # Субота
                congratulation_date += timedelta(days=2)
            elif weekday == 6:  # Неділя
                congratulation_date += timedelta(days=1)

            # 7. Додаємо результат у список у форматі рядка
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


# Приклад використання
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "John Wick", "birthday": "1964.09.02"},
    {"name": "Sandra  Bullock,", "birthday": "1964.07.26"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
