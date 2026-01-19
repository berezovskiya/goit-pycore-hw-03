from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    """
    визначає користувачів, чий день народження відбудеться протягом наступних 7 днів,
    враховуючи вихідні дні для дати привітання.
    """
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(
                year=today.year + 1)

        days_until = (birthday_this_year - today).days

        if 0 <= days_until <= 7:
            congratulation_date = birthday_this_year

            weekday = congratulation_date.weekday()
            if weekday == 5:  # Субота
                congratulation_date += timedelta(days=2)
            elif weekday == 6:  # Неділя
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "John Wick", "birthday": "1964.09.02"},
    {"name": "Sandra  Bullock,", "birthday": "1964.07.26"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
