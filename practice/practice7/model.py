import datetime
from datetime import date


class Date:
    """
    date
    """
    current_date: datetime

    def __init__(self, current_date=None) -> None:
        if not current_date:
            self.current_date = date.today()
        else:
            self.current_date = current_date

        new_year = date(self.current_date.year + 1, 1, 1)
        self.left = new_year - self.current_date

    @property
    def get_today(self):
        return f'today is {self.current_date}'

    def __str__(self):
        return f'{self.left.days} days to the New Year'


