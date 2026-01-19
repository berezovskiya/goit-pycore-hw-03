from datetime import datetime


def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        today_date = datetime.today().date()
        delta = today_date - given_date
        return delta.days

    except ValueError:
        print(
            f"Помилка: Формат дати '{date}' неправильний. Використовуйте РРРР-ММ-ДД.")
        return None


print(get_days_from_today("2028-10-09"))
