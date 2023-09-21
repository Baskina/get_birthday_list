from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    month_date_pattern = '%d %m'
    today = date.today()

    week_dates = [today]

    i = 1
    while i < 7:
        current_year = today.year
        timedelta_day = today + timedelta(days=i)
        timedelta_day_year = timedelta_day.year

        if current_year != timedelta_day_year:
            i += 1
            continue

        week_dates.append(timedelta_day)
        i += 1

    birthday_users = {}

    for user in users:
        user_birthday = user["birthday"]

        user_name = user["name"]

        for week_date in week_dates:
            if user_birthday.strftime(month_date_pattern) == week_date.strftime(month_date_pattern):

                day_key = 'Monday' if week_date.strftime('%A') == 'Saturday' or week_date.strftime(
                    '%A') == 'Sunday' else week_date.strftime('%A')

                if birthday_users.get(day_key) is not None:
                    birthday_users[day_key].append(user_name)
                else:
                    birthday_users[day_key] = [user_name]

    return birthday_users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()}
    ]

    result = get_birthdays_per_week(users)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
