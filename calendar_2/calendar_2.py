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

    def _filter_by_duration(self, **kwargs):
        events = []

        for event in self._events:
            attr = getattr(event, 'duration', None)
            if attr and attr in range(kwargs.get('min', 0), kwargs.get('max', attr + 1)):
                events.append(event)

        return events

    def _filter_by_title(self, **kwargs):
        events = []

        for event in self._events:
            attr = getattr(event, 'title', None)
            if attr and kwargs.get('search_text', '') in attr:
                events.append(event)

        return events

    def _filter_by_description(self, **kwargs):
        events = []

        for event in self._events:
            attr = getattr(event, 'description', None)
            if attr and kwargs.get('search_text', '') in attr:
                events.append(event)

        return events

    def _filter_by_owner(self, **kwargs):
        events = []

        for event in self._events:
            attr = getattr(event, 'owner', None)
            if attr and kwargs.get('search_text', '') in attr:
                events.append(event)

        return events

    def _filter_by_participants(self, **kwargs):
        events = []

        for event in self._events:
            attr = getattr(event, 'participants', None)
            if attr and kwargs.get('search_text', '') in attr:
                events.append(event)

        return events

    @staticmethod
    def sort_by_date(fn):

        def inner(*args, **kwargs):
            event = fn(*args, **kwargs)

            return sorted(event, key=lambda x: x.start_date)

        return inner

    @sort_by_date
    def filter(self, filter_name, **kwargs):
        options = {
            'duration': self._filter_by_duration,
            'title': self._filter_by_title,
            'description': self._filter_by_description,
            'owner': self._filter_by_owner,
            'participants': self._filter_by_participants,

        }

        return options.get(filter_name)(**kwargs)  # zadanie dla nas co tu ma byc (po ',')

    def remove(self, idx):
        events = list(filter(lambda x: x.idx == idx, self._events))

        if not events:
            raise ValueError(f'Can not delete element, because it does not exist')

        for event in events:
            self._events.remove(event)


    def __len__(self):
        return len(self._events)


data = generate_objects()

calendar = Calendar(data)

print(len(calendar))
c = calendar.remove(1)
print(len(calendar))


# f = calendar.filter_by_date()


# pprint(f)
# pprint(len(calendar))
# pprint(calendar.events)
