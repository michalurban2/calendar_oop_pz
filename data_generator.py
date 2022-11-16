import datetime
import random
import json
# paczki ze standard library, które są już wbudowane w python'a


class DataGenerator:
    def __init__(self, beginning_date, durations, titles, descriptions, users, reminder=False, workshop=False):
        self.beginning_date = beginning_date
        self.durations = durations
        self.titles = titles
        self.descriptions = descriptions
        self.users = users
        self.reminder = reminder
        self.workshop = workshop
        # tworzymy pola obiektu i przypisujemy zmienne

    def generate_data(self, amount):
        events = []

        for idx in range(amount):
            event = {
                'idx': idx,
                'start_date': f'{self.beginning_date + datetime.timedelta(hours=random.randint(1, 5000)):%Y/%m/%d, %H:%M}',
                'duration': random.randint(*self.durations),  # gwiazdka *, przekazujemy rozpakowaną tuple
                'title': random.choice(self.titles),
                'description': random.choice(self.descriptions),
                'owner': random.choice(self.users)
            }

            if self.reminder:  # jeżeli jest Trefy lub Falsy
                event['remind'] = random.choice([True, False])

            if self.workshop:
                event['participants'] = random.choices(self.users, k=random.randint(2, 20))

            events.append(event)

        return events

    @staticmethod
    def save_data(data, path):  # zapisywanie pliku
        with open(path, 'w') as file:
            json.dump(data, file)

    @staticmethod  # dodanie dekoratora staticmethod
    def load_data(path):  # wczytywanie pliku
        with open(path) as file:  # with jako kontekst
            return json.load(file)  # zwracamy metodo load w kontekście obiektu json


d = DataGenerator.load_data('event_data.json')
print(d)
