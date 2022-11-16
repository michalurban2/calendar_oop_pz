import datetime
from pprint import pprint

from event import Event, Workshop, Reminder
from helpers import generate_objects


class Calendar:
    def __init__(self, events=None):
        self._events = events or []

    @property
    def events(self):
        counter = 0

        for event in self._events:
            if datetime.datetime.now() < event.start_date <= datetime.datetime.now() + datetime.timedelta(weeks=4):
                counter += 1

        return f'You have {counter} events in four upcoming weeks.'

    @events.setter
    def events(self, value):
        if not isinstance(value, (Event, Workshop, Reminder)):
            raise TypeError(f'Provided value {type(value)} should be of type Event, Workshop or Reminder')

        self._events.append(value)

    def filter_by_date(self, start_date=datetime.datetime.min, end_date=datetime.datetime.max):
        events = []

        for event in self._events:
            if start_date <= event.start_date < end_date:
                events.append(event)

        return events

    def filter_by_duration(self, duration=None, duration_min=0, duration_max=None):
        if duration is not None:
            duration_min = duration_max = duration

        events = []

        for event in self._events:
            if event.duration in range(duration_min,
                                       (duration_max + 1 if duration_max is not None else event.duration + 1)):
                events.append(event)

        return events

    def __len__(self):
        return len(self._events)


data = generate_objects()

calendar = Calendar(data)
# f = calendar.filter_by_date(datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(weeks=2))
c = calendar.filter_by_duration(duration_min=15, duration_max=20, duration=15)

# f = calendar.filter_by_date()


# pprint(f)
# pprint(len(calendar))
# pprint(calendar.events)
