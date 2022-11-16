import datetime  # import paczki datetime
from pprint import pprint

from event import Event, Workshop, Reminder  # pascal case, gdyż są klasy wymienione po przecinku
from helpers import generate_objects


class Calendar:
    def __init__(self, events=None):  # events jest opcjonalny
        self._events = events or []  # tworzymy pole protected event, przypisujemy wartość events lub []
        # ^ OR zależy czy events będzie

    @property
    def events(self):  # metoda events z dekoratorem property, która czyni ją getterem
        counter = 0

        for event in self._events:  # pętla iteruje po polu obiektu protected events
            if datetime.datetime.now() < event.start_date <= datetime.datetime.now() + datetime.timedelta(weeks=4):
                # if sprawdza, start_date jest polem obiektu datetime
                counter += 1

        return f'You have {counter} events in four upcoming weeks.'

    @events.setter
    def events(self, value):
        if not isinstance(value, (Event, Workshop, Reminder)):
            raise TypeError(f'Provided value {type(value)} should be of type Event, Workshop or Reminder')

        self._events.append(value)

    def filter_by_date(self, start_date=datetime.datetime.min, end_date=datetime.datetime.max):  # minimalna data, i maxymalna data
        events = []

        for event in self._events:
            if start_date <= event.start_date < end_date:
                events.append(event)

        return events

    def filter_by

    def __len__(self):  # __len__ do sprawdzenia długości obiektu
        return len(self._events)  # wynik działania funkcji len


data = generate_objects()  # deklaracja zmiennej data i incjalizujemy ja wynikiem generate object

calendar = Calendar(data)  # wynik wywołana klasy Calendar
f = calendar.filter_by_date(datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(weeks=2))
# ^ deklaracja zmiennej f i wywołujemy funkcje filter_by_date(
# f = calendar.filter_by_date()

pprint(f)
pprint(len(calendar))
pprint(calendar.events)
