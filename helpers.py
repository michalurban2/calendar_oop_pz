import os
from datetime import datetime

from data_generator import DataGenerator
from event import Reminder, Workshop, Event


def generate_objects():
    abs_path = os.getcwd()
    data_obj = []
    files = ['event', 'reminder', 'workshop']
    for file in files:
        data = DataGenerator.load_data(os.path.join(abs_path, '..', f'{file}_data.json'))

        for item in data:
            item['start_date'] = datetime.strptime(item['start_date'], '%Y/%m/%d, %H:%M')

<<<<<<< HEAD
            if 'remind' in item:  # czy klucz remind znajduje się w słowniku
                data_obj.append(Reminder(**item))  # do listy obj dodajemy obiekt klasy Reminders
            elif 'participants' in item:  # czy jest participants klucz
                data_obj.append(Workshop(**item))  # inicjalizujemy obiekt klasy Workshop
=======
            if 'remind' in item:
                data_obj.append(Reminder(**item))
            elif 'participants' in item:
                data_obj.append(Workshop(**item))
>>>>>>> CO-003_calendar
            else:
                data_obj.append(Event(**item))

    return data_obj
