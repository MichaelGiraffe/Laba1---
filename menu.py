class Book:
    # Конструктор
    def __init__(self, title, price):
        self.title = title
        self.price = price

    # Запись в словарь
    def to_dict(self):
        return {
            "title": self.title,
            "price": self.price
        }

# Далее классы наследники
class Fairy_tale(Book):
    def __init__(self, title, price, good, evil):
        super().__init__(title, price)
        self.good = good
        self.evil = evil

    def to_dict(self):
        fairy_tale_dict = super().to_dict()
        fairy_tale_dict.update({
            "good": self.good,
            "evil": self.evil
        })
        return fairy_tale_dict


class Drama(Book):
    def __init__(self, title, price, place):
        super().__init__(title, price)
        self.place = place

    def to_dict(self):
        drama_dict = super().to_dict()
        drama_dict.update({
            "place": self.place,
        })
        return drama_dict

class Fantasy(Book):
    def __init__(self, title, price, world):
        super().__init__(title, price)
        self.world = world

    def to_dict(self):
        fantasy_dict = super().to_dict()
        fantasy_dict.update({
            "world": self.world
        })
        return fantasy_dict

class Techno_fantasy(Book):
    def __init__(self, title, price, technologies):
        super().__init__(title, price)
        self.technologies = technologies

    def to_dict(self):
        techno_fantasy_dict = super().to_dict()
        techno_fantasy_dict.update({
            "technologies": self.technologies,
        })
        return techno_fantasy_dict

class Dark_fantasy(Book):
    def __init__(self, title, price, necropolis):
        super().__init__(title, price)
        self.necropolis = necropolis

    def to_dict(self):
        dark_fantasy_dict = super().to_dict()
        dark_fantasy_dict.update({
            "necropolis": self.necropolis
        })
        return dark_fantasy_dict


class Science_fiction(Book):
    def __init__(self, title, price, obj):
        super().__init__(title, price)
        self.obj = obj

    def to_dict(self):
        science_fiction_dict = super().to_dict()
        science_fiction_dict.update({
            "object": self.obj,
        })
        return science_fiction_dict

class Historical(Book):
    def __init__(self, title, price, date):
        super().__init__(title, price)
        self.date = date

    def to_dict(self):
        historical_dict = super().to_dict()
        historical_dict.update({
            "date": self.date
        })
        return historical_dict

class Travelling(Book):
    def __init__(self, title, price, travel_place):
        super().__init__(title, price)
        self.travel_place = travel_place

    def to_dict(self):
        travelling_dict = super().to_dict()
        travelling_dict.update({
            "travel_place": self.travel_place,
        })
        return travelling_dict
