from datetime import datetime, timedelta


class Event:
    def __init__(self, start_date, duration, title, description, owner):
        self.owner = owner
        self.description = description
        self.title = title
        self.duration = duration
        self.start_date = start_date

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, new_duration):
        if not isinstance(new_duration, (int, float)):
            raise TypeError(f'Duration should be a positive digit. This is {type(new_duration)}.')

        if new_duration < 10:
            raise ValueError(f'too short event: {type(self).__name__} can not be shorter than 10 minutes.')

        self._duration = new_duration

    @property
    def start_date(self):
        return f'{self._start_date:%A %b %y, %H:%M}'

    @start_date.setter
    def start_date(self, new_start_date):
        if not isinstance(new_start_date, datetime):
            raise TypeError(f'Provided value is not date time: {type(new_start_date)}')

        if datetime.now() + timedelta(hours=1) > new_start_date:
            raise ValueError(f'{type(self).__name__} should not start in less than an hour')

        self._start_date = new_start_date

    def __str__(self):
        return f'{self.title}, {self.start_date}, ' \
               f'{(self._start_date + timedelta(minutes=self.duration)):%A %b %y, %H:%M}'

    def __repr__(self):
        attrs = ', '.join(
            f'{key[1:] if key.startswith("_") else key}={repr(value)}' for key, value in vars(self).items())
        return f'{type(self).__name__}({attrs})'
