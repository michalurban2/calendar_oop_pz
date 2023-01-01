from event import Event # z modułu(package) importujemy Klase Event


class Reminder(Event): # klasa Reminder, która dziedziczy z klasy Event
    def __init__(self, start_date, duration, title, description, owner, remind):  # init przyjmuje podane parametry
        super().__init__(start_date, duration, title, description, owner)
        self.remind = remind
class Reminder(Event):
    def __init__(self, idx, start_date, duration, title, description, owner, remind):
        super().__init__(idx, start_date, duration, title, description, owner)
        self.remind = remind
