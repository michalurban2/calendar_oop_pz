from event import Event


class Workshop(Event):
    def __init__(self, start_date, duration, title, description, owner, participants):
        super().__init__(start_date, duration, title, description, owner)
        self.participants = participants  # deklarujemy pole obiektu

    def __init__(self, idx, start_date, duration, title, description, owner, participants):
        super().__init__(idx, start_date, duration, title, description, owner)
        self.participants = participants
