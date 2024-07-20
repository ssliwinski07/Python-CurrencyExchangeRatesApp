import calendar


class Utilities:

    @staticmethod
    def get_month_days(year: int, month: int) -> int:

        _, num_days = calendar.monthrange(year=year, month=month)

        return num_days

    @staticmethod
    def clear_screen():
        print("\033c", end="")
